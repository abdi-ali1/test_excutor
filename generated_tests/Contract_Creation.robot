*** Settings ***
Library    custom_energy_keywords.custom_validations
Resource   ../resources/keywords.resource
Library    RequestsLibrary
*** Test Cases ***
Contract Creation
    [Tags]    contract    creation
    Load XML File    ${CURDIR}/context/contract_creation.xml
    Send POST Request    /api/contracts    ${xml_data}
    Validate Response Status    201
    Validate XML Schema    ${response_body}    schemas/contract_creation_schema.xsd