*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
testrest
    # Open Browser    https://sevasindhu.karnataka.gov.in/Sevasindhu/English      chrome
    ${x}=        Set Variable        2
    ${y}=        Set Variable        3
    ${z}=        Set Variable        ${x}+${y}
    # maximize browser window
    # input text    //input[@class='_2IX_2- VJZDxU']      1234567890
    # page should contain element         //button[text()='Request OTP']
    # sleep    5
    # close browser

