class LocatorsLogin:
    # Login page Objects

    username = 'username'
    sso_username_textbox_id = 'UserName'
    sso_relay_state_textbox_id = 'RelayState'
    password = 'password'
    LOGIN_BTN = 'submitButton'
    sso_single_signon_button_xpath = '/html/body/form/input'
    humanoid_id = 'profileButton'
    dc_coach_log_out_xpath = '/html/body/app/shell/div/header/div/div[3]/div[3]/div/span[2]/span'
    dc_driver_log_out_xpath = '/html/body/app/shell/div/header/div/div[3]/div/div/span[2]'
    fleet_log_out_xpath = '/html/body/app-root/shell/div/header/div/div[3]/div[3]/div/span[2]'
    dc_admin_log_out_xpath = '//*[text()="Sign Out"]'
    dvir_log_out_xpath = '/html/body/app-root/shell/div/header/div/div[3]/div[3]/div/span'
    my_account_button_xpath = '//*[@id="profileButton"]/parent::div//*[text()="My Account"]'
    lytx_logo_xpath = '/html/body/app-root/div[1]/img'
    sso_login_unsuccessful_xpath = '//*[contains(text(),"Login was unsuccessful.")]'

    # the xpath is different if login to driver safety
    login_success_lytx_logo_xpath = '/html/body/app-root/shell/div/header/div/div[1]/div'
    login_success_lytx_logo_dc_xpath = '/html/body/app/shell/div/header/div/div[1]/div'

    # select company
    company_textbox_id = 'company'
    company_tab_xpath = '/html/body/app-root/ng-component/mat-card/mat-card-content/form/div/mat-form-field/div/div[1]/div/input'
    selected_company_xpath = '/html/body/div/div/div/div/cdk-virtual-scroll-viewport/div[1]/mat-option/span'
    select_company_button_id = 'submitButton'

    profile_icon_implementation_center = '//label[contains(@class,"user")]'
    sign_out_btn_implementation_center = '// *[text() = "Sign out"]'