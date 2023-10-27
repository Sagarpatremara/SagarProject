*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://sevasindhu.karnataka.gov.in/Sevasindhu/English

*** Test Cases ***
Login to linkedin
    open browser    ${browser}      ${url}
    maximize browser window
    input text      //input[@id="twotabsearchtextbox"]      qweqrqereq
    capture page screenshot
