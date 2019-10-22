from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe', chrome_options=chrome_options)

pageNum = 10001

while pageNum <= 10005:
    try:
        driver.get(f"https://movie.naver.com/movie/bi/mi/basic.nhn?code={pageNum}")
        select_genre = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a').text
        select_country = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(2) > a').text
        select_runningtime = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(3)').text
        select_date = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(4)').text
        select_director = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4) > p > a').text
        select_actor1 = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p > a:nth-child(1)').text
        select_actor2 = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p > a:nth-child(2)').text
        select_actor3 = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6) > p > a:nth-child(3)').text
        select_grade = driver.find_element_by_css_selector('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a').text
        select_actor = [select_actor1, select_actor2, select_actor3]

    except:
        print(select_genre, select_country, select_runningtime, select_date, select_director, select_actor,
              select_grade)
        pageNum += 1

'''
 자동화 시키기 위해서 먼저 네이버 영화의 페이지 순서대로 갖고오도록 했지만
 조건문 이후에 잘못된게 있어서 차례대로 갖고 오지 못함 수정 
'''
