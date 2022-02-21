# Xencapital-UI
Xencapital UI automation

## Environment
- macOS
- Python `3.9`
- pip `21.3.1`
- Selenium `4.1.0`
- pytest 
- allure-pytest
- Allure `2.17.3`

### More Details

#### #Allure
1. Download [Allure](https://github.com/allure-framework/allure2/releases/tag/2.17.3)
2. Unzip Allure file
3. Configure environment variables
    ```shell=zsh
    vim /Users/xen/.zprofile
    ```
   Add the path of the bin folder of allure
   ```
   # allure
   PATH="Your allure directory/bin:${PATH}"
   export PATH
   ```
   Make the .zprofile effective
   ```shell=zsh
   source  /etc/profile
   ```
   Verify whether the environment variable is added successfully
   ```shell=zsh
   allure --version
   ```