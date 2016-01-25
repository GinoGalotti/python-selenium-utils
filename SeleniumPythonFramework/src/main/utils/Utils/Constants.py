__author__ = 'ginogalotti'


class TestingConstants():
    # Test_Data
    EXPECTED_URL_AFTER_LOGIN = "/data/mine"
    EXPECTED_URL_PRICING = "/pricing"
    EXPECTED_URL_MAGIC = "magic."
    EXPECTED_URL_EXAMPLES = "examples"
    EXPECTED_URL_ERROR_EXTRACT = "error"
    EXPECTED_URL_RESET_PASSWORD = "resetpassword"
    EXPECTED_URL_RESET_CONFIRMATION = "resetconfirmation"

    MAGIC_HIGHLIGHT_URL_EXAMPLE = {"url": "http://www.ikea.com/us/en/search/?query=chair", "number_rows": 22}
    MAGIC_TRY_OUT_URL_EXAMPLE = {"url": "http://redditlist.com/", "url_part": "redditlist"}
    MAGIC_EXTRACT_VALID_EXAMPLE = {"url": "http://m.reddit.com/r/data", "url_part": "m.reddit.com"}
    MAGIC_EXTRACT_INVALID_EXAMPLE = {"url": "http://i.reddit.cof"}

    EXPECTED_MAIL_TEXT_IN_ERROR_LOGIN = "email is not registered"
    EXPECTED_RESET_PASSWORD_TEXT = "Reset email sent, please check your email and click on the link"
    EXPECTED_NO_API_TEXT = "APIs you create appear here"
    EXPECTED_MAGIC_API_NAME = "Magic Api"
    EXPECTED_MAGIC_NO_DATA_TEXT = "compatible with every site, sometimes we need a little extra input"

    CHANGE_NAME_USER = {"user": "changing_name_user@4null.com", "pass": "mportiotesting"}
    CHANGE_MAIL_USER = {"user": "changeemailtestaccount", "pass": "mportiotesting"}
    IMPORT_NOAPI_USER = {"user": "testingnoapi@4null.com", "pass": "mportiotesting"}
    IMPORT_API_USER = {"user": "testingwithapi@4null.com", "pass": "mportiotesting", "number_api": 3,
                       "active_api_name": "Magic Api"}
    SEND_PASSWORD_USER = {"user": "testing.send.import@gmail.com", "pass": "mportiotesting"}
    IMPORT_NEW_API_USER = {"user": "testingnewapi@4null.com", "pass": "mportiotesting"}
    IMPORT_LOGIN_PROD = {"user": "ginog", "pass": "importiotesting"}
    IMPORT_LOGIN_STAGE = {"user": "ginog@gino.com", "pass": "mportiotesting"}
    GOOGLE_LOGIN = {"user": "importiotesting@gmail.com", "pass": "mportiotesting"}
    FACEBOOK_LOGIN = {"user": "importiofacetesting@gmail.com", "pass": "QAtesting"}
    GITHUB_LOGIN = {"user": "importiogittesting@gmail.com", "pass": "QAt3sting"}
    LINKEDIN_LOGIN = {"user": "importiolinktesting@gmail.com", "pass": "QAtesting"}


class FrameworkConstants():
    STAGING_ENV = "staging"
    PRODUCTION_ENV = "production"

    # MAC_CHROMEDRIVER_PATH = "../../../../../../chromedriver/chromedriverMac"                # Local testing
    MAC_CHROMEDRIVER_PATH = "chromedriver/chromedriverMac"
    LINUX_CHROMEDRIVER_PATH = "chromedriver/chromedriverLinux64"
    DEFAULT_PASSWORD = "testing"
