#CSS SELECTOR
from selenium.webdriver.common.by import By
# 주소
WebIsaURL = "https://24ro.co.kr/www-dev/"
ttee = By.XPATH, "/html/body/div[1]/div/div[1]/form/fieldset/div/div/input"

#랜딩 팝업
PopupContents = '#main > div > div.imgArea > div.popupArea > div'
PopupContents_Applogo = '#main > div > div.imgArea > div.popupArea > div > img'
PopupContents_SubTitle = '#main > div > div.imgArea > div.popupArea > div > p.sub-title'
PopupContents_MainTitle01 = '#main > div > div.imgArea > div.popupArea > div > p:nth-child(3)'
PopupContents_MainTitle02 = '#main > div > div.imgArea > div.popupArea > div > p:nth-child(4)'
PopupContents_MainTitle03 = '#main > div > div.imgArea > div.popupArea > div > p:nth-child(5)'
PopupContents_AppBtn = '#main > div > div.imgArea > div.popupArea > div > div'
PopupContents_CloseText = '#main > div > div.imgArea > div.popupArea > div > p.close-text'

#메인화면 사이드 요소
Side_QrcodeArea = '#main > div > div.textArea > div.qrcodeArea > img'
Side_Title1 = '#main > div > div.textArea > div.titleArea > div.title-container > div.firstTitle_full > p.title1'
Side_Title2 = '#main > div > div.textArea > div.titleArea > div.title-container > div.firstTitle_full > p.title2'
Side_SecondTitle = '#main > div > div.textArea > div.titleArea > div.secondTitle'
Side_ChatText01 = '#main > div > div.chatArea > p.chat-text01'
Side_ChatText02 = '#main > div > div.chatArea > p.chat-text02'
Side_IconChat01 = '#main > div > div.chatArea > p.kakaoChat > img'

############################################################메인화면############################################################
#배너
Banner001 = '#root > div > div.css-exb7bi.es91q9021 > div.css-1pbms9s.es91q9015 > div.adm-swiper.adm-swiper-horizontal > div.adm-swiper-track.adm-swiper-track-allow-touch-move > div > div:nth-child(1) > div > div > img'
Banner002 = '#root > div > div.css-exb7bi.es91q9021 > div.css-1pbms9s.es91q9015 > div.adm-swiper.adm-swiper-horizontal > div.adm-swiper-track.adm-swiper-track-allow-touch-move > div > div:nth-child(2) > div > div > img'
Banner003 = '#root > div > div.css-exb7bi.es91q9021 > div.css-1pbms9s.es91q9015 > div.adm-swiper.adm-swiper-horizontal > div.adm-swiper-track.adm-swiper-track-allow-touch-move > div > div:nth-child(3) > div > div > img'
BannerCounter = '#root > div > div.css-exb7bi.es91q9021 > div.css-1pbms9s.es91q9015 > div.adm-swiper.adm-swiper-horizontal > div.css-2tzkng.es91q9013'
#원하는 서비스를 선택하세요
ChooseServiceText = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1wyu670.es91q9019 > span'
ChooseServiceText02 = '/html/body/div[1]/div/div[1]/div[3]/div[1]/text()'
#이사
ServiceIconText01 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-zl1inp > div > div > div:nth-child(1) > div > p.css-1a7kpdb'
ServiceIconText02 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-zl1inp > div > div > div:nth-child(1) > div > p.css-15kxs6z'
ServiceIconCar = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-zl1inp > div > div > div:nth-child(1) > div > img'
#운송
OnlyMoveText01 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-zl1inp > div > div > div:nth-child(2) > div > p.css-1a7kpdb'
OnlyMoveText02 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-zl1inp > div > div > div:nth-child(2) > div > p.css-15kxs6z'
OnlymoveIconCar = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-zl1inp > div > div > div:nth-child(2) > div > img'
#---------------------------------------
#사진 견적 3단계 꿀팁!
PhotoTip = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div:nth-child(3) > div > p'
PhotoTipBanner01 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1fv59ds.es91q9014 > div > div > div.adm-swiper-track.adm-swiper-track-allow-touch-move > div > div:nth-child(1) > div > div > img'
PhotoTipBanner02 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1fv59ds.es91q9014 > div > div > div.adm-swiper-track.adm-swiper-track-allow-touch-move > div > div:nth-child(2) > div > div > img'
PhotoTipBanner03 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1fv59ds.es91q9014 > div > div > div.adm-swiper-track.adm-swiper-track-allow-touch-move > div > div:nth-child(3) > div > div > img'
PhotoTipPagination01 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1fv59ds.es91q9014 > div > div > div.adm-swiper-indicator > div > div.adm-page-indicator-dot.adm-page-indicator-dot-active'
PhotoTipPagination02 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1fv59ds.es91q9014 > div > div > div.adm-swiper-indicator > div > div:nth-child(2)'
PhotoTipPagination03 = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1fv59ds.es91q9014 > div > div > div.adm-swiper-indicator > div > div:nth-child(3)'
###이사하는 내 방 사진 찰칵!###
MovingMyroomB = '#root > div > div.css-p4yw3f.e165y051 > div > div.adm-nav-bar-left > div > span.adm-nav-bar-back-arrow > div > img'
MovingMyroomTitle = '#root > div > div.css-p4yw3f.e165y051 > div > div.adm-nav-bar-title > p > span'
MovingMyroomSTitle01 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-1mj04r2.e7sbnmn6 > p.css-1cvwd93'
MovingMyroomSTitle02 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-1mj04r2.e7sbnmn6 > p.css-1nv8xy1'
MovingMyroomStep01 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-10juk0a.e7sbnmn5 > p.css-1v548x9'
MovingMyroomTipTitle = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-10juk0a.e7sbnmn5 > p.css-8d9jrl'
MovingMyroomPhoto01 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-jrazg9.e7sbnmn4 > img:nth-child(1)'
MovingMyroomPhoto02 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-jrazg9.e7sbnmn4 > img:nth-child(2)'
MovingMyroomPhoto03 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-jrazg9.e7sbnmn4 > img.css-41zask'
MovingMyroomTip01Icon = '#root > div > div.css-135fybp.e7sbnmn7 > div:nth-child(4) > div > p > img'
MovingMyroomTip01Text = '/html/body/div/div/div[2]/div[4]/div/p/text()'

MovingMyroomPhoto04 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-1xx5gug.e7sbnmn2 > img'
MovingMyroomTip02Icon = '#root > div > div.css-135fybp.e7sbnmn7 > div:nth-child(6) > div > p > img'
MovingMyroomTip02Text = '/html/body/div/div/div[2]/div[6]/div/p/text()'

MovingMyroomPhoto05 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-b0q2c9.e7sbnmn3 > img:nth-child(1)'
MovingMyroomPhoto06 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-b0q2c9.e7sbnmn3 > img.css-1diuroh'
MovingMyroomPhoto07 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-b0q2c9.e7sbnmn3 > img.css-b3w3v3'
MovingMyroomPhoto08 = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-b0q2c9.e7sbnmn3 > img:nth-child(4)'
MovingMyroomTip03Icon = '#root > div > div.css-135fybp.e7sbnmn7 > div.css-1d19wkz.e7sbnmn1 > div > p > img'
MovingMyroomTip03Text = '/html/body/div/div/div[2]/div[8]/div/p/text()'
MovingMyroomEnd = '/html/body/div/div/div[2]/div[9]/p/text()[1]'
MovingMyroomEnd2 = '/html/body/div/div/div[2]/div[9]/p/text()[2]'
#---------------------------------------

#---------------------------------------
#나만 몰랐던! 이사의 진실
TruthTitle = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div:nth-child(5) > div > p > span'
TruthTitle1 = '/html/body/div[1]/div/div[1]/div[3]/div[5]/div/p/text()'
ImageOfTruth = '#root > div > div.css-exb7bi.es91q9021 > div.css-jv9j2.es91q9020 > div.css-1ndw5x4.es91q902 > img'
###나만 몰랐던 이사의 진실###
TruthB = '#root > div > div.css-p4yw3f.e165y051 > div > div.adm-nav-bar-left > div > span.adm-nav-bar-back-arrow > div > img'
TruthInTitle = '#root > div > div.css-p4yw3f.e165y051 > div > div.adm-nav-bar-title > p > span'
TruthSTitle1 = '#root > div > div.css-v5abgj.eiqq12g6 > div.css-f0ew4t.eiqq12g5 > p.css-z8djt8'
TruthSTitle2 = '#root > div > div.css-v5abgj.eiqq12g6 > div.css-f0ew4t.eiqq12g5 > p.css-1kunp0a'

TruthFirstTitle = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div:nth-child(1) > p > span.css-alojyt'
TruthFirstTitle2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div:nth-child(1) > p > span.tip-title-text'
TruthFirstImage = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > img'
TruthFirstImage2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div.css-l41x6v.eiqq12g3 > p.css-dscuvu'
TruthFirstImage3 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div.css-l41x6v.eiqq12g3 > p.css-ybazat'
TruthFirstTip = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div:nth-child(4) > p > img'
TruthFirstTip2 = '/html/body/div/div/div[2]/div[2]/div[3]/p/text()'
TruthFirstTipIcon1 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div.css-m9famu > img'
TruthFirstTipDes1 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div.css-m9famu > div'
TruthFirstTipIcon2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div.css-d952c7 > img'
TruthFirstTipDes2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(2) > div.css-d952c7 > div'

TruthSecondTitle = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div:nth-child(1) > p > span.css-alojyt'
TruthSecondTitle2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div:nth-child(1) > p > span.tip-title-text'
TruthSecondImage = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > img'
TruthSecondImage2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div.css-l41x6v.eiqq12g3 > p.css-dscuvu'
TruthSecondImage3 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div.css-l41x6v.eiqq12g3 > p.css-ybazat'
TruthSecondTip = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div:nth-child(4) > p > img'
TruthSecondTip2 = '/html/body/div/div/div[2]/div[3]/div[3]/p/text()'
TruthSecondTipIcon1 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div.css-m9famu > img'
TruthSecondTipDes1 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div.css-m9famu > div'
TruthSecondTipIcon2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div.css-d952c7 > img'
TruthSecondTipDes2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(3) > div.css-d952c7 > div'

TruthThirdTitle = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div:nth-child(1) > p > span.css-alojyt'
TruthThirdTitle2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div:nth-child(1) > p > span.tip-title-text'
TruthThirdImage = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > img'
TruthThirdImage2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div.css-e6rdg4.eiqq12g2 > p.css-dscuvu'
TruthThirdImage3 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div.css-e6rdg4.eiqq12g2 > p.tip-second-text.css-ybazat'
TruthThirdTip = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div:nth-child(4) > p > img'
TruthThirdTip2 = '/html/body/div/div/div[2]/div[4]/div[3]/p/text()'
TruthThirdTipIcon1 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div.css-m9famu > img'
TruthThirdTipDes1 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div.css-m9famu > div'
TruthThirdTipIcon2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div.css-d952c7 > img'
TruthThirdTipDes2 = '#root > div > div.css-v5abgj.eiqq12g6 > div:nth-child(4) > div.css-d952c7 > div'

TruthEnd = '#root > div > div.css-v5abgj.eiqq12g6 > div.css-hx7nhd.eiqq12g1 > img'
#---------------------------------------







