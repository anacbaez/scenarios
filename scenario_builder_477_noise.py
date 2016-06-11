__author__ = 'Kiryl Trembovolski'

from selenium import webdriver
import selenium
import time

def xpath_finder_wrapper(link):
    while True:
        try:
            output = driver.find_element_by_xpath(link)
        except selenium.common.exceptions.NoSuchElementException:
            continue
        break
    return output

def login(username, password):

    username_button = driver.find_element_by_id("login-username")
    password_button = driver.find_element_by_id("login-password")
    login_button = driver.find_element_by_id("login-button")

    username_button.send_keys(username)
    password_button.send_keys(password)

    time.sleep(1)

    login_button.click()

    time.sleep(6)

    scenarios_button = xpath_finder_wrapper("//div[text()='Scenarios']")

    scenarios_button.click()

    time.sleep(2)

def add_scenario_code(word, scenario_script):

    scenario_code = xpath_finder_wrapper("//textarea[@class='v-textarea v-widget v-textarea-error v-form-field v-textarea-v-form-field v-textarea-required v-required v-has-width']")
    scenario_code.send_keys(scenario_script % word.lower())

    time.sleep(2)

def add_scenario_name(word, count):

    scenario_name = xpath_finder_wrapper("//input[@class='v-textfield v-widget v-textfield-error v-form-field v-textfield-v-form-field v-textfield-required v-required v-has-width']")
    scenario_name.send_keys("hotlist_"+ str(count))

    time.sleep(2)

def choose_me_group(me_group):

    me_group_button = xpath_finder_wrapper("//select[@class='v-select-twincol-options']/option[text()='%s']" % me_group)
    me_group_button.click()

    time.sleep(2)

    choose_me_group_button = xpath_finder_wrapper("//div[@class='v-select-twincol-buttons']/div[1]")
    choose_me_group_button.click()

    time.sleep(2)

    save_changes_button = xpath_finder_wrapper("//span[text()='save changes']")
    save_changes_button.click()

    time.sleep(2)

def add_scenario(word, scenario_script, count):

    add_button = xpath_finder_wrapper("//section[@class='v-actionbar v-widget open v-actionbar-open v-has-height']/div[2]/ul/li[1]/span[2]")
    add_button.click()

    time.sleep(4)

    add_scenario_code(word,scenario_script)

    add_scenario_name(word, count)

    me_groups_button = xpath_finder_wrapper("//div[@class='dialog-root v-widget dialog-panel dialog-root-dialog-panel v-has-width v-has-height']/div/div[2]/div/div[2]/div/ul/li[2]/div[1]")
    me_groups_button.click()

    time.sleep(2)

    choose_me_group(me_group)

if __name__ == '__main__':

    list_of_words = [['bhvx:1_k4BZKP1zBzMAABqV', 'bhvx:1_B2UtKa2AvuUAAEjl', 'bhvx:1_ZyRUl8H8SRgAAArR', 'bhvx:1_1vkDWr79Pz4AAAr2', 'bhvx:1_d5ct/WKTE4gAABX7', 'bhvx:1_iKxs0IxxG1cAAxNC', 'bhvx:1_1fLtHY1F1OwAAEcW', 'bhvx:1_iNTdS/LNsuQAAAsP', 'bhvx:1_DEj6IL22XZ0AAEf7', 'bhvx:1_2XOw5ZcE0kQAABDk'], ['bhvx:1_8oB9UTRKNlgAAAoM', 'bhvx:1_GdqTFmInPTgAAEcl', 'bhvx:1_gpeuxUcWqAEAAHU8', 'bhvx:1_k3L2U03V0FYAAAnN', 'bhvx:1_IOOfFjBMz4YAABP7', 'bhvx:1_iwlHGdo//oAAAf+v', 'bhvx:1_MdQqLY159TsAAAsQ', 'bhvx:1_SHWR0igNrXwAAAs8', 'bhvx:1_EjkiHcfVrPcAAAd2', 'bhvx:1_YWgustVHr50AAEsZ'], ['bhvx:1_fibpudcvKKUAAAjJ', 'bhvx:1_/D0S9aQbrEYAACKZ', 'bhvx:1_40wasg8AuEsAAA0g', 'bhvx:1_BCQkJtWUZ8cAAAiy', 'bhvx:1_ZTam/ZaDKuAAAAi1', 'bhvx:1_HQFsrqBbWLcAAEdv', 'bhvx:1_DlUsAiM170UAAAiy', 'bhvx:1_AsoXfMEWOhkAACYL', 'bhvx:1_VtiSSx5b70cAAEY4', 'bhvx:1_Gyy1Sa8XOnkAAA7b'], ['bhvx:1_kyUBu8TRkkYAAAm1', 'bhvx:1_mT/qsTPwpG4AAAdk', 'bhvx:1_jjBAoo8DEysAActj', 'bhvx:1_XvlU33GRbZYAAEd0', 'bhvx:1_swyIT4/8onkAAEqG', 'bhvx:1_DzOZSzTMXs8AAAun', 'bhvx:1_oqu5x4bQqg0AAAob', 'bhvx:1_cNo9iUgNpysAAApD', 'bhvx:1_y19TAI5lsQwAAAqe', 'bhvx:1_r+CWCMs3kV4AAAlQ'], ['bhvx:1_Ld9+OL3ZSmoAADDS', 'bhvx:1_3VPLQ9JT874AAAzu', 'bhvx:1_ZApeGeKtRGEAAArV', 'bhvx:1_4nkP0hcf5AUAAAnU', 'bhvx:1_w+vh2UQalI0AAAqZ', 'bhvx:1_OOnb01lJkKgAAAde', 'bhvx:1_tWEFwLgzCPUAAAqz', 'bhvx:1_c9LgkT5f4TgAAEpV', 'bhvx:1_ny41a1j7PnkAAH5m', 'bhvx:1_IG4AbMZIjRQAAA3e'], ['bhvx:1_fRFP+1ReOc4AADGI', 'bhvx:1_i+k39EH8UhMAAAle', 'bhvx:1_BYcGctEzabkAAAdK', 'bhvx:1_vnh8aOtdkSUAAApJ', 'bhvx:1_S1Ybjv8hJiwAAEHd', 'bhvx:1_6cig/fN28BcAAAfZ', 'bhvx:1_XEFlJsFo7rEAACVO', 'bhvx:1_uaUX0/V++24AAAuG', 'bhvx:1_cnIhTDscaNsAABM2', 'bhvx:1_m5tzilZgxyIAAAdd'], ['bhvx:1_nS6ShHiguYMAAAn+', 'bhvx:1_49QQbH17H98AAAZf', 'bhvx:1_fDMoDs9x+ZgAAJwR', 'bhvx:1_OJrGIc9rE1YAAAhO', 'bhvx:1_BFTh7UkOBZUAADKf', 'bhvx:1_KaxcgaVFv+8AAEgk', 'bhvx:1_LgHLXxMXHDoAACXM', 'bhvx:1_rJHnfWIuwpcAABe+', 'bhvx:1_L2/rNnTy+soAADse', 'bhvx:1_oCAQEIafqjYAAAkv'], ['bhvx:1_JZL9dSTMjdIAAAtE', 'bhvx:1_IJdvAp25j+MAAAkJ', 'bhvx:1_LVpnaFJYRwYAAC1O', 'bhvx:1_3oenpFB503kAABhX', 'bhvx:1_RGcH3Yzr7QAAABqb', 'bhvx:1_/XTmX+cpSaAAAC0i', 'bhvx:1_dmLJx64XK9sAAIFw', 'bhvx:1_vuIvNRkNB2AAAElL', 'bhvx:1_BY24Gr3PYtwAAAq3', 'bhvx:1_8Qvu+ZoZVS8AABCB'], ['bhvx:1_EFYcFTiVPuQAAAsX', 'bhvx:1_FBC5voDC8GQAAAg7', 'bhvx:1_Sf0WjzcewqQAABay', 'bhvx:1_m6BjV4IEX68AAEdv', 'bhvx:1_Mga5ZPutUdEAAEiP', 'bhvx:1_f1KzxlDqoVkAAET0', 'bhvx:1_lRr4DgU9WSUAACz7', 'bhvx:1_8/3xCdqIdxAAAAw+', 'bhvx:1_96GEcuqND6UAAEfw', 'bhvx:1_v48HajD/e4wAAExS'], ['bhvx:1_Yi+94UzGbqcAAAew', 'bhvx:1_sY7lkIOC+rQAAAnB', 'bhvx:1_8YtbwteXk2gAAfMw', 'bhvx:1_Rp5jRQY9zF0AAEjX', 'bhvx:1_5Xd596NbycYAAA2r', 'bhvx:1_0OKzmX1ZgScAAAnN', 'bhvx:1_5ZLhUMZvItoAAEPj', 'bhvx:1_pMyf4Evi6pAAAH9w', 'bhvx:1_pIuREC/ceQQAAEr2', 'bhvx:1_mzq3kcGCd64AAICc'], ['bhvx:1_aKUr2Bj0NrsAAVbO', 'bhvx:1_4IfKUCkDhMwAAEem', 'bhvx:1_p+zCJFfsJwUAAEc9', 'bhvx:1_DfSaCMECOg8AAAdj', 'bhvx:1_Pg7FtLFLQ08AAEJv', 'bhvx:1_uyu/vIstjF0AAEP7', 'bhvx:1_an962GhLdnEAAAnd', 'bhvx:1_CiUhygysSLsAAAv8', 'bhvx:1_0NynRwDi1RkAAHx6', 'bhvx:1_YwCsWJ1h/WYAAAqN'], ['bhvx:1_CxRBPG9MBysAAAtt', 'bhvx:1_sPzscC+9yJgAAEcT', 'bhvx:1_Oj7vFI0C3wEAABDO', 'bhvx:1_wyS2M6Tlw1cAAAro', 'bhvx:1_39CmvjRLbT0AAAnY', 'bhvx:1_OppWZ8gWL5EAAEe9', 'bhvx:1_T4sUZDYi3KYAACZQ', 'bhvx:1_CpacgLqoROQAABBL', 'bhvx:1_x0uFEtfxQWQAAcFF', 'bhvx:1_AP8Pn1bTn80AAJjp'], ['bhvx:1_U8EyviJctGsAAEjB', 'bhvx:1_a8N4NKVc29YAAAw8', 'bhvx:1_anTqSvTcQp0AAQhi', 'bhvx:1_O0mAlCf4/ewAABDE', 'bhvx:1_YFbzzIbYjMcAADDj', 'bhvx:1_+XHJ+EtpuGQAAAmR', 'bhvx:1_eOkuAaGt+GUAABTm', 'bhvx:1_wqllwVrk9BkAAEiz', 'bhvx:1_RcyfY4YPh9MAADE4', 'bhvx:1_BWb3rAx5WzAAAEBm'], ['bhvx:1_9XsEDctH9tAAAEc9', 'bhvx:1_CSXoXo/R2ekAAEhU', 'bhvx:1_CLMyLtOni2MAAI+K', 'bhvx:1_mrTjTwqGmKUAAAg5', 'bhvx:1_PQuHofI8tboAAJ7C', 'bhvx:1_wToSychchMAAAAmJ', 'bhvx:1_Db1RdduwspkAAAub', 'bhvx:1_QKOEWK4LQ/kAAEfB', 'bhvx:1_0nwF5bJlU9sAAAnN', 'bhvx:1_Z1NfIibggQgAAEkB'], ['bhvx:1_RRzWD8PsefUAAAsY', 'bhvx:1_bZslGXyFIc4AAvLY', 'bhvx:1_hOigWvoURNYAAAwY', 'bhvx:1_cubKTcBip78AAAst', 'bhvx:1_ga+E4LMx4W4AAEio', 'bhvx:1_6/L7XDFMSK4AAA3h', 'bhvx:1_Xwg4EsbJrk8AAElD', 'bhvx:1_e7hYNdWRVB8AAExM', 'bhvx:1_5ysZmoF4vsQAAcsH', 'bhvx:1_tMun5eVW/wgAAAwp'], ['bhvx:1_dds2LY3msL8AACo1', 'bhvx:1_u9fQ7ALWSZ4AAEg7', 'bhvx:1_g339tNaltI0AAArk', 'bhvx:1_mQ+7dQ6aFasAAEMt', 'bhvx:1_9fl0A46DTL0AAAnV', 'bhvx:1_RUlOpYDleaEAAAnx', 'bhvx:1_NdOyxDaPXzYAAEKj', 'bhvx:1_ETcCLP9cJGoAABiS', 'bhvx:1_Cl3tn0ytI3oAAe7L', 'bhvx:1_mbccbfU+hQkAAEsx'], ['bhvx:1_0d1TreIiJiwAAEbT', 'bhvx:1_tjy/Quai0KsAAEjz', 'bhvx:1_AYy5Mt+dndUAAEeo', 'bhvx:1_9+p0H0abh8wAAElv', 'bhvx:1_3oaliQkeYKwAAAXl', 'bhvx:1_4QVu2K+JWPYAAAoX', 'bhvx:1_4QmxUjwUhCcAAA2F', 'bhvx:1_qDnz/gUd1DMAAH7e', 'bhvx:1_HIz7snBMXhoAAAgO', 'bhvx:1_DuHrTosV2AAAAEaO'], ['bhvx:1_AkCsB4N0CMAAAAhd', 'bhvx:1_9eMOvbRGdUYAAEWl', 'bhvx:1_/IwJJ9BkIR8AABcu', 'bhvx:1_2D5SIk6+ARAAAA7N', 'bhvx:1_quq51+2mtU4AAAgd', 'bhvx:1_dKHVJPgMRnsAAAlW', 'bhvx:1_i8NWrnCsMowAABUx', 'bhvx:1_duuFQY0S4h4AAA4+', 'bhvx:1_6RzuQe1aBTYAAEt3', 'bhvx:1_pFQhJIJCyfEAAEkN'], ['bhvx:1_oE77YaDUv+0AAEb5', 'bhvx:1_bF0JxqAqtPAAAAhC', 'bhvx:1_zHwzmzpvpT4AAK/P', 'bhvx:1_nRMy4WsPuJgAABWK', 'bhvx:1_N+wa0YlxrVMAAAkp', 'bhvx:1_VN8PNvGg1TsAAEIS', 'bhvx:1_Mtzl5ypN/FQAABsI', 'bhvx:1_J682TMZLidIAAAcr', 'bhvx:1_zSrMofJbLU0AAAhW', 'bhvx:1_qMLmkEZMefEAAAz5'], ['bhvx:1_I4xt7vZQmWMAAEkF', 'bhvx:1_J7zRwBgimfwAAB/I', 'bhvx:1_omgCFKCnslgAAAnJ', 'bhvx:1_RHkyExmkBugAAAhc', 'bhvx:1_PksvFOGk4fEAAEQq', 'bhvx:1_wZYH/nlDNd0AADLk', 'bhvx:1_mEHgw7Vnn08AAAfe', 'bhvx:1_CaDXF11MyTIAABLQ', 'bhvx:1_7gGvi1dcDkAAAArF', 'bhvx:1_L6tG3Xdu6uUAAAn6'], ['bhvx:1_qab+el0ORXYAAEib', 'bhvx:1_7aAs/vF/HSEAAA29', 'bhvx:1_H3+M15UoiKYAABDh', 'bhvx:1_qFxGXoQDxfoAAAnZ', 'bhvx:1_jW9xMe/48yYAAAso', 'bhvx:1_/DvaToIwNukAAEgM', 'bhvx:1_A8IvXIW6xFQAAb2u', 'bhvx:1_m28JLzGnhGoAAAiz', 'bhvx:1_m6lOoAB9TYEAAAoE', 'bhvx:1_9u5YQZxguFQAAEfV'], ['bhvx:1_Nv+Ib2TJBeoAAAoR', 'bhvx:1_9KQyYC6r2YUAAFiU', 'bhvx:1_OPYa+KV6G/QAAEld', 'bhvx:1_eYCY4qB6STYAAEZd', 'bhvx:1_/KfZPtiJpCAAABYj', 'bhvx:1_7LyNsU7qJcUAAeea', 'bhvx:1_4qQNKm+3CeQAAKUc', 'bhvx:1_lDJ4P1oBa7oAAEff', 'bhvx:1_OVI2+tDfWtkAAA1J', 'bhvx:1_wOXk3lvOx6UAAEMB'], ['bhvx:1_eZ+1ZdxAGrwAAEJn', 'bhvx:1_MBWVSOCkZz0AAEin', 'bhvx:1_0EZXZQe27ksAAAdd', 'bhvx:1_xvw7CCBjiv4AADXP', 'bhvx:1_/tNKTi8ir4YAACsH', 'bhvx:1_yC+E0yAWvlsAAHuZ', 'bhvx:1_oLZwgGckJZgAAAbe', 'bhvx:1_qNDih61YulwAADbh', 'bhvx:1_qT5yjszkCYMAAfyc', 'bhvx:1_xXLjrwd4kRkAAEw8'], ['bhvx:1_JmVN9S4hRokAAAgk', 'bhvx:1_DfBrIumN7cUAAEBt', 'bhvx:1_cWu/HsBCag0AAAgh', 'bhvx:1_x45QDJceWEMAAICu', 'bhvx:1_gmvkNVeQ7loAAK2G', 'bhvx:1_s7Hbn6STF5sAAAxs', 'bhvx:1_CVHaNKbB+PIAAEJa', 'bhvx:1_2lPzKeWod+AAAB1E', 'bhvx:1_1Iv9Q0VzbycAABNA', 'bhvx:1_acUG9JJtux8AAAkj'], ['bhvx:1_bJL5RvvPC5EAABDG', 'bhvx:1_i+obuA3AxuAAAJVr', 'bhvx:1_equrKksMBfsAAJ4k', 'bhvx:1_zZf4wXJO0P8AAchu', 'bhvx:1_qztpj9kyu+8AAEcX', 'bhvx:1_kWJHfjdfCjoAAEtH', 'bhvx:1_lypwraT1Q9gAAAnP', 'bhvx:1_aM0k144ZhIEAACyG', 'bhvx:1_cHlg6V29LMwAAApK', 'bhvx:1_ubQaR0m85ikAALfg'], ['bhvx:1_0Jdv0OI8U24AAEk1', 'bhvx:1_RaCLfNDdEK0AAAkF', 'bhvx:1_mIf8CvaQItIAAAnJ', 'bhvx:1_Mzn39cnQjAwAAC1N', 'bhvx:1_CTCYDbUrkOoAAEez', 'bhvx:1_oO9bv1YPAxEAAEMZ', 'bhvx:1_BG0TV/9VITcAAI86', 'bhvx:1_dj9DUAjJ8kQAAApf', 'bhvx:1_0h0/MB7nQUkAAEh9', 'bhvx:1_TWa/Fhv2TBoAABAR'], ['bhvx:1_OgCokYXaNo0AAxWj', 'bhvx:1_LFQd2rplOk4AAEeV', 'bhvx:1_LS29GQWpmCEAABBa', 'bhvx:1_6XUUPftGOxEAABkW', 'bhvx:1_+lx7DvZYGlgAACdK', 'bhvx:1_Jmu85SKgTkgAAEGi', 'bhvx:1_HIK7gYgE+qUAAAuP', 'bhvx:1_KmArKlUDgr0AAEgj', 'bhvx:1_vnZZMWNPvkwAAJge', 'bhvx:1_1oxA+N/sQdIAACsw'], ['bhvx:1_wM/A5iyUnUcAAAnP', 'bhvx:1_SYpHeL6PHYUAAEdk', 'bhvx:1_8TSr7/9lqXUAAA0s', 'bhvx:1_bK+orsWB56UAAEsZ', 'bhvx:1_y1jNXRSEOAQAAAzk', 'bhvx:1_+OQYEMK8gmEAAcL8', 'bhvx:1_8nKd+C8T0qwAAAiL', 'bhvx:1_lA3kGdoac0EAAEF7', 'bhvx:1_81hDVub6bpYAAEfF', 'bhvx:1_HKSdSOAWXuEAAAsy'], ['bhvx:1_4Fi5Mh1pTRIAAAmS', 'bhvx:1_4oz5YLd5ebkAAAyB', 'bhvx:1_R4EA0gD5Y7MAAAjH', 'bhvx:1_v1KYoLgaqEcAAAsN', 'bhvx:1_UIc4jBrwA7QAAA95', 'bhvx:1_NJDc9Vac2tQAAAlY', 'bhvx:1_j53yDmcWggQAAA1e', 'bhvx:1_KcXGhudIH9AAAApF', 'bhvx:1_8ufag6FzTXoAAEdQ', 'bhvx:1_bsChk+IcWgEAAApZ'], ['bhvx:1_fHm0OomYguYAAIIY', 'bhvx:1_NgVAxXcMP3IAABe5', 'bhvx:1_8IjPQ3wrDhEAAAbd', 'bhvx:1_hPnhCijyevQAAAfZ', 'bhvx:1_5keiA9XVIWAAAES+', 'bhvx:1_6n0FE4T8wFgAABsS', 'bhvx:1_tyNjE/UCT0sAAL5d', 'bhvx:1_qYPCfdHiclUAAAod', 'bhvx:1_WmD5M4X49S8AAEZM', 'bhvx:1_v7/2ScZUlkYAAC1K'], ['bhvx:1_fF+OX+l0y84AAEVm', 'bhvx:1_8Et5UIeVgVoAACux', 'bhvx:1_CNkkTO99NCwAAAll', 'bhvx:1_EhJB19BriR8AAEZA', 'bhvx:1_A/3GBNF59iEAADEl', 'bhvx:1_uH/gCfnDweoAAEko', 'bhvx:1_jA9z9UW/vCwAAAwY', 'bhvx:1_XpuZ+qb/DHcAAEhf', 'bhvx:1_jfE15p1Ty3cAAEN7', 'bhvx:1_5IIdvVCJ9pYAAEYX'], ['bhvx:1_qiNc6PrFwWYAADg3', 'bhvx:1_BbHcIU9lPYoAACiK', 'bhvx:1_Cd47fD7sjX4AAEpi', 'bhvx:1_iZlqMEs+lb8AAClv', 'bhvx:1_QQWudfBHSX0AAEfx', 'bhvx:1_Fc+jNRWsfhkAAEgp', 'bhvx:1_NWbg7hCrSV0AAEjH', 'bhvx:1_o1kSd6noAFYAAEgP', 'bhvx:1_vPX53ja9eKoAAEYH', 'bhvx:1_WBn3wEiRUsMAAAtd'], ['bhvx:1_tAaxy68JOD8AACtd', 'bhvx:1_551Gh/vr8QkAAH0z', 'bhvx:1_gVRuOqh7ab4AAA0W', 'bhvx:1_/HIFG7pi/OMAAENr', 'bhvx:1_bpo2zqYPFQgAAAq8', 'bhvx:1_MwroVLKoAGkAADvv', 'bhvx:1_LgnqSYpeaTUAAA+6', 'bhvx:1_QG4YWSpvj9sAAAdb', 'bhvx:1_lEax/YnsAHQAADCU', 'bhvx:1_tVu407RsFSEAAAsW'], ['bhvx:1_chJX2naGjgMAAB9A', 'bhvx:1_RzzQJSuyUX0AALW3', 'bhvx:1_OEbCvGTXe4QAAAzO', 'bhvx:1_pMoRDLhWV9MAAAhW', 'bhvx:1_l/Y9h6n/5Y8AAAb/', 'bhvx:1_0q6c/5wa558AABob', 'bhvx:1_k9djdo74sVgAAAhc', 'bhvx:1_i1MaaH5eHrYAABoS', 'bhvx:1_o/wYQSZIapcAAuvp', 'bhvx:1_VLZ3FHm3Qq8AAAci'], ['bhvx:1_TGmBzfptausAABml', 'bhvx:1_XM9mvwjMqmcAAGZP', 'bhvx:1_pP4ah0hb+IkAAuk4', 'bhvx:1_WCP4YZQ9+H4AAAgf', 'bhvx:1_baLvKwpLLUoAAAkc', 'bhvx:1_R2Ud+oaAnogAABfd', 'bhvx:1_wdAZ/CZn1PcAABpv', 'bhvx:1_zDYZK9a/XZAAABWB', 'bhvx:1_EA7kSduUGhgAAAdT', 'bhvx:1_29hf3oKlZnEAAAfV'], ['bhvx:1_3KxDyAeJdSsAABuT', 'bhvx:1_1C9kKxxwpk8AAAd/', 'bhvx:1_D0eMnAK9vV8AAAhQ', 'bhvx:1_wkX6XGzIL4YAAEKn', 'bhvx:1_QoBdgvVWd1sAAAeS', 'bhvx:1_0UJbBdcc29oAAunl', 'bhvx:1_OXy/ebB5F1UAAAeg', 'bhvx:1_uaCjr/cPP1QAAAds', 'bhvx:1_uGafSSWVoPEAAAoE', 'bhvx:1_Vm/iHqrDkwUAAAe4'], ['bhvx:1_iAux6ELFi6AAAAfH', 'bhvx:1_EirfUSmIFAAAAAgS', 'bhvx:1_68rD5XB/b9kAAAeN', 'bhvx:1_KLbYMsQA0tMAABn5', 'bhvx:1_EBemerS2vk0AAuk5', 'bhvx:1_BeylURip0PQAABuz', 'bhvx:1_syjWg4fg2tgAAAg9', 'bhvx:1_JJXi8ihuc0sAABly', 'bhvx:1_CCIz6Iie47MAABo3', 'bhvx:1_OTDgMxnV0pcAABsr'], ['bhvx:1_RzUPM5PIgwQAAAee', 'bhvx:1_j865QYqecyUAAAfo', 'bhvx:1_RyyeVVpAbvkAAAdq', 'bhvx:1_au7BYUVwzDYAABl4', 'bhvx:1_wzoGo6VUXbcAAAhL', 'bhvx:1_9kco80eMUy4AAAdE', 'bhvx:1_7luQmenUFLAAAuZ3', 'bhvx:1_/BgM1vX2F/sAAD9s', 'bhvx:1_JycGUsRv4YYAAu60', 'bhvx:1_mp6XnLTomD8AABo/'], ['bhvx:1_u9NmhEPqSeIAAAfy', 'bhvx:1_vq64sEhUcpQAAAeL', 'bhvx:1_kFokx4NCN18AAuvu', 'bhvx:1_WiRryPiGavgAAukv', 'bhvx:1_wujGIJX4T8UAAAlc', 'bhvx:1_1JB51oH7xy4AAuvy', 'bhvx:1_fsGBFvQrsmYAABdI', 'bhvx:1_3nsRYA95aNUAABVp', 'bhvx:1_1b1ESzfSbS4AAAcz', 'bhvx:1_6T/xdOnI5JUAAAeC'], ['bhvx:1_Qd6wiZFT5/YAAB2V', 'bhvx:1_xrl91QLQVQYAAAhD', 'bhvx:1_xUUC5dzZBEEAABpy', 'bhvx:1_MRkmbUBfqqIAAuk1', 'bhvx:1_cH6WcrJhoM4AAAfR', 'bhvx:1_lJ88+/kWYUsAAuk1', 'bhvx:1_KPudAnk111YAABlk', 'bhvx:1_9iVP06ebTEAAAAh2', 'bhvx:1_SjbP2DGttmgAABmC', 'bhvx:1_SNQvWfpvbHIAABb4'], ['bhvx:1_CKwJROfGTAoAAAdu', 'bhvx:1_x4JNzwTwIEkAABc7', 'bhvx:1_rbqoaiImMysAAuk9', 'bhvx:1_4kJxczk6k8wAAAeG', 'bhvx:1_7rZMzl1KvIkAABio', 'bhvx:1_lWoeA1uvt9kAABrV', 'bhvx:1_eIv7Zu5gqYMAAGZ4', 'bhvx:1_ub2o7NST/GgAAD/Q', 'bhvx:1_dXIRohJ7zegAABmF', 'bhvx:1_z2TvB5iPRAQAABko'], ['bhvx:1_BY3ZYn63qnkAAAia', 'bhvx:1_DRcxRWxxxsIAABve', 'bhvx:1_mmOlholoo4MAAAgM', 'bhvx:1_afyL7KCLpSUAABnd', 'bhvx:1_AWqvn1u0ViQAAu6i', 'bhvx:1_yBUleTChp2QAABhz', 'bhvx:1_0yNEs+Ke/Y4AAAdU', 'bhvx:1_kQ9Z71O5GqEAABgq', 'bhvx:1_0lJzrkAUsJwAAEKD', 'bhvx:1_42+Pmu349LgAABnp'], ['bhvx:1_TLVLNrfxc74AAXEG', 'bhvx:1_8Ruok0hwMScAAAj3', 'bhvx:1_szayK9LbJB4AABj8', 'bhvx:1_bgveefB7/UMAAuZ6', 'bhvx:1_dJAP3mPnaNAAAAe/', 'bhvx:1_eUQr/BsDE2YAAAd4', 'bhvx:1_Ao+SqqKdQEoAABdE', 'bhvx:1_YaBGK2jOTz0AAAeB', 'bhvx:1_+on5uB1vbv4AABmz', 'bhvx:1_d9BACb83CLUAAAd0'], ['bhvx:1_pAf1XTr9phsAABfV', 'bhvx:1_mT8BEI0nN0wAAD9U', 'bhvx:1_KBt5HmvhjtkAAAdF', 'bhvx:1_Wp8zakRCPKEAABrR', 'bhvx:1_rqTRPHnproMAABlh', 'bhvx:1_3D819YbEKr0AABoY', 'bhvx:1_f0hb5MVDfqYAAAh4', 'bhvx:1_J0Lhv46K0sAAABo6', 'bhvx:1_WNrrO0kCdkQAAvQj', 'bhvx:1_pq6+KNWEigIAAuk8'], ['bhvx:1_57drHDbBHpsAABhq', 'bhvx:1_h32omOQBpuMAABpg', 'bhvx:1_UVynA0mKhZAAABrF', 'bhvx:1_WVcWEE4tDl4AABVd', 'bhvx:1_mjxIcXX8NeEAAAe8', 'bhvx:1_NDUTtioPpdEAABm/', 'bhvx:1_OSt3WGMTFTEAAApJ', 'bhvx:1_Ir3AFY8jsp4AAAgX', 'bhvx:1_hrfxJe8JfBQAAukv', 'bhvx:1_6+P6khyns0oAABmu'], ['bhvx:1_BUpUYYZ7Q04AAAkh', 'bhvx:1_55MN7Uq10NMAABdb', 'bhvx:1_mQ7M/nzOdG0AAAej', 'bhvx:1_gWd/H4THnHcAAAgR', 'bhvx:1_QVx4ubZpdfYAABnF', 'bhvx:1_YjDfk+7PxwUAAAf9', 'bhvx:1_KB8XuZfFsioAAAke', 'bhvx:1_59vpGc6XSxoAADx3', 'bhvx:1_lRLwkoWRWjkAAAia', 'bhvx:1_QbLpJx0N/A8AAAdA'], ['bhvx:1_QsMqLIZldKIAAAia', 'bhvx:1_veHx9a2DZB0AAAgb', 'bhvx:1_qZ3GfCZqupoAABdX', 'bhvx:1_NIp9plf8vUQAAAdk', 'bhvx:1_lt4nmjZCe3MAAD9z', 'bhvx:1_SIOsKIHRCnUAAuO4', 'bhvx:1_jmqwYj0ZWtsAABpc', 'bhvx:1_Zc0oWAsRAwkAAAhb', 'bhvx:1_ze2/oJWD7YcAAAs+', 'bhvx:1_kyvVRZQW1XoAAAd1'], ['bhvx:1_sQTX6AvFWvMAAuk5', 'bhvx:1_F3jAKxPBFNoAAEKt', 'bhvx:1_sTwd0pTYSHkAAAeu', 'bhvx:1_WCW2W+czPiUAAAgB', 'bhvx:1_QfMM/XmnThIAABpc', 'bhvx:1_0bGodtVOQGUAAAfK', 'bhvx:1_Q1yAUdqSzfAAAAjT']]


    scenario_script = "Text (value = \"%s\") /+5 EntityList(type = text, name = \"financial_entities\") AND Relationship(type = closeness, value = 1 .. 100) AND ((Content-Info(field = participant_count, value < 9) AND Content-Info(field = type, value = email)) OR NOT Content-Info(field = type, value = email))"
    me_group = "ALL"

    driver = webdriver.Chrome("/Users/anabaez/Google Drive/Tullett Prebon/Scenarios/scripts/chromedriver")
    driver.get("http://10.239.2.131:8081/admin/.magnolia/admincentral#app:beh-security:;")

    login("k.trembovokski", "Behavox2015")

    #cycle starts here
    start_time = time.time()

    for word in list_of_words:
        time.sleep(2)
        idx = list_of_words.index(word)
        word = '" "'.join(word)
        add_scenario(word, scenario_script, idx)

    finish_time = time.time()-start_time

    print "Execution time: ", finish_time/float(60)

    driver.quit()