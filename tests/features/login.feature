Feature: Login page

  @smoke @positive @only
  Scenario: Login
    Given Open page
    When Login email = "yanushevskayaelena132@gmail.com"
    Then See terminal

  Scenario: Open chat
    Given Open page
    When Open chat
    Then See chat

  Scenario Outline: Languages
    Given Open page
    When Change language "<lang>"
    Then Page translated on "<lang>" and text visible "<expect>"

    Examples:
      | lang          | expect       |
      | Bahasa Melayu | Teruskan     |
      | Čeština       | Pokračovat   |
      | Dansk         | Fortsæt      |
      | Deutsch       | Fortfahren   |
      | Español       | Continuar    |
      | Français      | Continuer    |
      | Italiano      | Continua     |
      | 中国的           | 继续           |
      | ไทย           | ดำเนินการต่อ |

  Scenario: Login wrong user
    Given Open page
    When Login email = "123@gmail.com"
    Then See failed notification

  @only
  Scenario: Forgot password
    Given Open page
    When Forgot password
    Then See new page "Password recovery - RoboForex Ltd", "https://my.roboforex.com/en/remind/"

  Scenario Outline: Open login page from FR
    Given Open page from FR
    Then Page opened on "<lang>" and text visible "<expect>"

    Examples:
      | lang     | expect    |
      | Français | Continuer |
