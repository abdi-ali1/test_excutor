*** Settings ***
Library    RequestsLibrary
Library    libraries.custom_energy_keywords.custom_validations

*** Keywords ***
Load XML File
    [Arguments]    ${file_path}
    ${xml_data}=    Get File From Library    ${file_path}
    Set Suite Variable    ${xml_data}

Send POST Request
    [Arguments]    ${endpoint}    ${body}
    Create Session    api_session    http://192.168.1.159:8000
    &{headers}=    Create Dictionary    Content-Type=application/xml
    ${response}=    POST On Session    api_session    ${endpoint}    data=${body}    headers=&{headers}
    Set Suite Variable    ${response_body}    ${response.text}
    Set Suite Variable    ${response_status}    ${response.status_code}

Send DELETE Request
    [Arguments]    ${endpoint}    ${body}
    Create Session    api_session    http://localhost:8000
    &{headers}=    Create Dictionary    Content-Type=application/xml
    ${response}=    DELETE On Session    api_session    ${endpoint}    data=${body}    headers=&{headers}
    Set Suite Variable    ${response_body}    ${response.text}
    Set Suite Variable    ${response_status}    ${response.status_code}

Send PUT Request
    [Arguments]    ${endpoint}    ${body}
    Create Session    api_session    http://localhost:8000
    &{headers}=    Create Dictionary    Content-Type=application/xml
    ${response}=    PUT On Session    api_session    ${endpoint}    data=${body}    headers=&{headers}
    Set Suite Variable    ${response_body}    ${response.text}
    Set Suite Variable    ${response_status}    ${response.status_code}

Validate Response Status
    [Arguments]    ${expected_status}
    Validate Response Status From Library    ${expected_status}

Validate XML Schema
    [Arguments]    ${xml_content}    ${schema_file}
    Validate XML Schema From Library    ${xml_content}    ${schema_file}
