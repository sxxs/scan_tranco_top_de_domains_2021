# Tracking on Top 1000 .de domains

Analysis of popular German websites according to the Tranco Top 1M list (https://tranco-list.eu). Selection criteria: first 1012 domains ending with “.de”. Scans took place between Apr 19 18:22 and Apr 20 18:35 2021.

Note that a scan of “.de” domains is not exactly equivalent to the set of “most popular German site operators”.

The analysis was carried out with privacyscanner (https://github.com/PrivacyScore/privacyscanner) that instruments a Chrome browser. Every page was scanned with a fresh Chrome profile. Chrome was restarted before every scan.

**TLDR: Of the scanned 1012 domains, 382 domains exhibit behavior that indicates that they are tracking user activities before consent.**

Note that this number includes sites *with* cookie consent banners but also sites *without* consent banners. 

TODO: The initial scan does not contain the necessary data to determine the presence of consent banners after the scan.



### Dataset Breakdown

Total domains: 1012

Domains with errors: 44

Domains with at least one third party request: 681

Domains with third party requests where at least one third party attempts to set a cookie: 398

**To avoid false positives, we focus on requests to known trackers according to the EasyPrivacy list.**

Domains with third party requests to known trackers: 672

Domains with third party requests to known trackers where at least one third party attempts to set a cookie: 371 


**We did not analyze whether third parties carried out browser fingerprinting yet.**


### Cookies

Of the 382 domains that exhibit tracking, 308 domains set a cookies to a third-party tracking domain. We only looked at cookies that contain enough entropy to hold a value that could be used as fingerprint. In particular, we only cosider these 8 cookie domains (incl. number of calling domains that set this cookie):

.ioam.de (**187**)  
.doubleclick.net (**44**) *[name: IDE]*  
.consensu.org (**24**) *[name: __cmpconsent]*  
responder.wt-safetag.com (**13**)  
m.exactag.com (**12**)  
.google.com (**9**) *[name: NID]*  
.rubiconproject.com (**6**) *[name: rsid]*  
.yandex.com (**6**) *[name: i]*  

Note that some of these domains, in particular consensu.org (which belongs to the IAB), seem to be related with consent management. consensu.org, however, sets cookies with large random content that cannot be distinguished from unique identifiers.


### Tracking URL Requests

Further, we include consider domains to track their users if they include traffic to known tracking providers:

https://www.google-analytics.com/j/collect? (**141**)  
https://www.google-analytics.com/collect? (**39**)  
https://pagead2.googlesyndication.com/pagead/gen (**17**)  
https://googleads.g.doubleclick.net/pagead/viewthroughconversion (**13**)  
https://www.econda-monitor.de/l/ (**9**)  
https://googleads4.g.doubleclick.net/pcs/view? (**3**)  


Note that we observed 118 requests (by approximately 118 sites) to Google Analytics without enabled Anonymize IP functionality (aip=1). AIP was deemed mandatory by data protection authorities in the past. You can check AIP for any site on your own here: https://checkgoogleanalytics.psi.uni-bamberg.de/

Command to obtain an estimate of missing AIP:

```
cat abstract.json | fgrep "https://www.google-analytics.com/" | fgrep "collect?" |fgrep -v aip=1 | wc -l
118
```

Note that according to the current (April 2021) opinion of data protection authorities (https://www.datenschutzkonferenz-online.de/media/dskb/20200526_beschluss_hinweise_zum_einsatz_von_google_analytics.pdf), Google Analytics cannot be used at all without giving prior consent.


## Example Cases for Illustration


### Cookies

**ioam.de (187)**

source: spiegel.de

```
{
"url": "spiegel.de",
"rank": 4,
"cookies": [
  {
    "domain": ".ioam.de",
    "name": "i00",
    "value": "003c6e707beda536a607daea10001%3B607daea1%3B61eee0c6"
  }
],
```

**.doubleclick.net (44)**

source: dw.de

```
{
"domain": ".doubleclick.net",
"name": "IDE",
"value": "AHWqTUnnvUbhPlDuWiHyHjH1MEhNkZUCPTXR9b5Va3ubjpCVo9DkL6qHyEzOv__HKPE"
},
```

**.consensu.org (24)**

source: abendblatt.de

```
{
"domain": ".consensu.org",
"name": "__cmpconsentx14486",
"value": "CPE8dXQPE8dXQAfHmCDEBWCgAAAAAH_AAAYgFtQAQFtAdSQn0OkZNcUBxeHlAyxQohBfWVFcBZAIIFIEBIAFAAoCwlAQQQAAABKCAIAIBDgCiVgEAAEAMQAQAAQBAAAQAAaQBAASAAAggAkAAAAEAQAAACAAAAAAAAAAAAAmABACQEEADwoAEYCCAgDAAABAgCACAgAECAgFAwAIC2goAEBbQcACAtoSABAW0LAAgLaGgAQFtDwAIC2iIAEBbRMACAtoqABAW0A"
},
```

**responder.wt-safetag.com (13)**

source: zeit.de

```
{
"domain": "responder.wt-safetag.com",
"name": "wt_nbg_Q3",
"value": "!i4KIurQpx1V1tQOrbKgImUoBMap0L84tYsF+2ehUdZNga4fkhkXy/ZXCQGC7lQRSCIs071Z8ZpOjbZ4="
}
```

**m.exactag.com (12)**

source: bahn.de

```
{
"domain": "m.exactag.com",
"name": "exactag_new_gk",
"value": "a8ceece154774f39b9728334f31e2dfe%7c18.06.2021+16%3a40%3a45"
},
{
"domain": "m.exactag.com",
"name": "session_session",
"value": "d634c954c46e42849f2cae6e"
},
{
"domain": "m.exactag.com",
"name": "exactag_new_user",
"value": "1053%7c2%7cd634c954c46e42849f2cae6e%7c01.01.0001+00%3a00%3a00%7c19.04.2021+16%3a40%3a45%7cd634c954c46e42849f2cae6e%7c68537%7c1753%7cFalse"
},
```

**.google.com (9)**

source: pinterest.de

```
{
"domain": ".google.com",
"name": "_GRECAPTCHA",
"value": "09ANblmng-FbMdNMD2m1GuLV1KeXNrF_oQkbIz3jcE0Ngfxf_Cz2ddglPXuj98xYOFT7VcwoX9seeWXvI7xq2d6f8"
},
{
"domain": ".google.com",
"name": "NID",
"value": "213=YmTKbIgZ8auvMz0Eqbf3bJmOLJ0KIMaQzhpWQr16EEnZWOZcUdiswa-1w2wCJaWMD1jurOHqc2XeyV_Mkf1HAVfpB_m95rx50eSho1RLHGSz4yQme406xe38jnBEFKzS76472zCGMNp1AAW2jbd4LHlBaBU2SBX8Q2aMHhNjvWU"
}
```

**.rubiconproject.com (6)**

source: dw-world.de

```
{
"domain": ".rubiconproject.com",
"name": "rsid",
"value": "1|G9CqJlwMr/XFWmao0M0uNhnwoIJYaqCajCF8XMCkfko2/NzCYnq3HobfN+PO17aJGUjo/mjrHzC2UVinXkmqADT+pWwGnm1Zo0d7O5rhFBstoAWhCKFbOsXyJLrbN17/CLvxkBIPaHCflKhtI7Rjmc5wWfekKj+fSLsm8pxVD53Cs8fO6aB19eiJ131Sr8qUFzJg67PkMGQ="
},
{
"domain": ".rubiconproject.com",
"name": "audit",
"value": "1|hLZGFuTafB3PxMbxkA4yi6QPH/I72/+TmyZ/11wQL9HnwIwbYRvuYxFMKYgrV2f64HEYI5ehIrVD3bTJYnIwotzpQ7vzkXQ/"
},
```

**.yandex.com (6)**

source: akadem-ghostwriter.de

```
{
"domain": ".yandex.com",
"name": "yuidss",
"value": "3168960151618922188"
},
{
"domain": "mc.yandex.com",
"name": "yabs-sid",
"value": "373913841618922188"
},
{
"domain": ".yandex.com",
"name": "i",
"value": "zmJ6wkFpgQd2NdTGdhzQ32Jxl6W6//HNXqAVBlMlgGvSqjtAtolAf+W5Ugb1lOF8I2Wf7VT15qiBFq2B9GI+J8CIUTs="
},
{
"domain": ".yandex.com",
"name": "ymex",
"value": "1650458188.yrts.1618922188#1650458188.yrtsi.1618922188"
},
```


### Requests to Well-known Trackers

**https://www.google-analytics.com/j/collect? (141)**

source: ebay-kleinanzeigen.de

```
https://www.google-analytics.com/j/collect?v=1&_v=j89&aip=1&a=1499129103&t=pageview&_s=1&dl=https%3A%2F%2Fwww.ebay-kleinanzeigen.de%2F&dp=https%3A%2F%2Fwww.ebay-kleinanzeigen.de%2F&ul=en-us&de=UTF-8&dt=eBay%20Kleinanzeigen%20%7C%20Kostenlos.%20Einfach.%20Lokal.%20Anzeigen%20gratis%20inserieren%20mit%20eBay%20Kleinanzeigen&sd=24-bit&sr=800x600&vp=785x585&je=0&_u=aGBAAAIJCAAAAC~&jid=945175548&gjid=128838255&cid=300623226.1618849490&uid=&tid=UA-24356365-9&_gid=1329624884.1618849490&_r=1&_slc=1&cd1=Homepage&cd2=&cd3=&cd6=&cd7=&cd8=&cd9=&cd10=&cd11=&cd12=&cd13=&cd15=de_DE&cd25=97-js-errorlog_A%7CBLN-18532_highlight_B%7CBLN-18276-k8s-stats-ui_B%7CBLN-18275-lazy-load-image_A%7CDesktop_Test_B%7Creact-msgbox-payment-buy_B%7Creact-msgbox-payship_B%7CBLN-18685_auth_svr_A%7Cspeedcurve-labs-lux-1_A%7Cgdpr-experimental_C%7Cspeedcurve-labs-lux-2_C%7CBLN-18221_srp_rebrush_ads_B%7C76-preact-header-footer_A%7C74-react-messagebox_A%7CEBAYKAD-2252_group-assign_B&cd28=distribution_test-c%3Byo_s-D%3Bliberty-experimental-DEFAULT%3Bliberty-experimental-2-DEFAULT%3BLib_A%3B&cd50=(NULL)&cd53=&cd90=&cd91=&cd94=&cd95=&cd96=&cd97=&cd125=distribution_test-c&cd128=yo_s-D&cd130=liberty-experimental-DEFAULT&cd131=liberty-experimental-2-DEFAULT&cd135=Lib_A&cd73=0&cd69=300623226.1618849490&z=276539755
```

**https://www.google-analytics.com/collect? (39)**

source: t-online.de

```
https://www.google-analytics.com/collect?v=1&_v=j89&aip=1&a=1111288536&t=event&ni=1&_s=1&dl=https%3A%2F%2Fwww.t-online.de%2F&ul=en-us&de=UTF-8&dt=News%20%26%20E-Mail%20bei%20t-online.de%20%7C%20Politik%2C%20Sport%2C%20Unterhaltung%20%26%20Ratgeber&sd=24-bit&sr=800x600&vp=800x600&je=0&ec=consent%20management&ea=display&el=2021-01-14-cmp-test-e5-2&ev=0&_u=aHDAAEALAAAAAC~&jid=&gjid=&cid=575547055.1618849516&tid=UA-89731071-12&_gid=209537858.1618849516&gtm=2wg472P9FVTRJ&cg1=undefined&cd1=Page&cd2=undefined&cd3=DSL%2CT-DSL%2CTelefonbuch%2CRoutenplaner%2CNachrichten%2CSpiele%2CShopping%2CService&cd4=46&cd5=&cd6=&cd7=unknown&cd8=desktop&cd9=News%20%26%20E-Mail%20bei%20t-online.de%20%7C%20Politik%2C%20Sport%2C%20Unterhaltung%20%26%20Ratgeber&cd10=Home&cd11=t-online.de&cd12=unknown&cd13=unknown&cd14=unknown&cd15=undefined&cd16=undefined&cd17=&cd18=&cd19=&cd20=575547055.1618849516&cd21=unknown&cd22=desktop&cd23=live&cd24=2&cd25=2&cd26=undefined&cd27=undefined&cd28=undefined&cd29=0&cd30=&cd31=16.04.2021&cd32=startseite&cd33=unknown&cd46=&cd47=11.02.2010%2013%3A26%3A07&cd48=11.02.2010&cd49=undefined&cd50=undefined&cd51=undefined&cd52=40018267%2C40000061%2C40000049%2C40000039&cd57=00-th-startseite-ID46&cd59=undefined&cd60=Kommentare%20AUS&cd61=unknown&cd66=undefined&cd67=unknown&cd68=unknown&cd69=&cd70=unknown&cd71=100&cd72=ohne%20Fotoshow&cd73=unknown&cd74=0&cd75=0&cd76=unknown&cd77=unknown&cd88=0&cd89=undefined&cd90=undefined&cd91=undefined&cd92=undefined&cd93=t-online.de&cd95=&cd96=&cd97=&cd102=0&cd103=0&cd104=unknown&cd105=unknown&cd106=unknown&cd107=unknown&cd108=unknown&cd109=2021-01-14-cmp-test-e5-2&cd111=unknown&cd112=unknown&cd113=no-consent-state&cd114=no-consent-state&cd116=no-consent-state&cd35=undefined&cd36=undefined&cd37=undefined&cd38=undefined&cd39=undefined&cd40=undefined&cd41=undefined&cd42=undefined&cd43=undefined&cd44=undefined&cd45=not%20set&cd55=undefined&cd56=undefined&z=1227558789
```

**https://pagead2.googlesyndication.com/pagead/gen (17)**

source: mydealz.de

```
https://pagead2.googlesyndication.com/pagead/gen_204?id=sodar2&v=222&t=2&li=gpt_2021041501&jk=2217026885238877&bg=!NjWlNXHNAAZUuIlwVLg7ACkAdvg8WiaTCITWcKpSmBgrNcER8XeS8_wJPyA_PtIk0ttFKB89zOwXDQIAAAFKUgAAABJoAQcKAPTkc0PbqlEwjBfa5zzoqjKIrRkjqd2m42jtlDKPyPrALQpSMZHfDk1YAs7kAfMWw5wS8w3oKdSD9eN24-ZY9uPU3Bh-ty8cCIXlwNc6DpiPtXEPIyInxOeyNz5C7Eam5uYwX8d7m4PHhAICCHlxZcXkyjDoqj12bz_V2I2LEoZLsKIjpUI0CCu-BajadQxG7Oxzu0MUkkOVWfU1D5dMQ_0WAFowBhq3c44JiLajCXlH6byTJEzcv7Nint019EOECWoVDzyBOi4ojYSMspdxt6QnqDMbU9qZpDp87NM8pDrOdPY-OzdyDHczOyRV0HYb6Ip_7-CnmQIWk6EdLpZ_jcA0mc8DroT3naIhOzWjhXSJ7XtfVWgkyVrArKFMu0EnIanesnpwSTioiO9oE9P8eJ3QKAMkkk5_nz4VGtoiescQ3YQcdKbUllvuRwrFCy840vAnHuIPFF2MPbuw45BvjzLWfeDEmpaadILKd0xWxjIDIEtW-7ke-FE7Rza4lqqUV2LDWyXnTfQXnDhZlodoknk3a-HKxYhS-aXEGqQnnh1ueHcbHY1Ut_MkkhkNxHfvO2aw1Bo9bBZxhxBb2Lg4EA4KQnJqFMBmIPT3fpbiYJ9ln0JbUW8Aqc2Zs5Lv_n06qY6ppowfeAJDQVfnQQy4Yxgg3Lpd8DFyAUz2ciF8tv-LTmSaPpVMLfyAA9RxO7Lu44xZrCd6kzWLsaD_BWIwhoDa73sJMWyT73qFABKMrdLizO83PTaZACA3C0t8PNkbpY6Xn5ARrCuImeXVifof6veHti-WCZVw0zEUj_3IBf4kJAJ2f1J67WTfxCR5jTdrVWDtrYipOeT7aubzdKs6JTvrzywSJ5QKP6xq2a6o0uLJTF8iHrAiGVTilwvbyILc8BeG7Q30xjO0Qq-PM9YrryjVtmUqKodBMEZeU_hG0z16wXMWsId7su9EgHUUUD9-NZz8lb-tknoW_3U3YViAvjXoq8Lqobdx1IYtbQpomUJcYiBcXoXU2CXMrvAUMoT_pQV1HeleJQ664aPk3A8E
```

**https://googleads.g.doubleclick.net/pagead/viewthroughconversion (13)**

source: beepworld.de

```
https://googleads.g.doubleclick.net/pagead/viewthroughconversion/1069068836/?random=821531425&fst=1618909265500&num=1&value=0&label=Xp42CN7f_wEQpOTi_QM&bg=666666&hl=en&guid=ON&resp=GooglemKTybQhCsO&eid=2505059651&u_h=600&u_w=800&u_ah=600&u_aw=800&u_cd=24&u_his=2&u_tz=120&u_java=false&u_nplug=0&u_nmime=0&sendb=1&ig=1&frm=0&url=https%3A%2F%2Fbeepworld.de%2F&tiba=Eigene%20Homepage%20erstellen%20-%20kostenlos%20mit%20Beepworld&hn=www.googleadservices.com&fmt=3&ctc_id=CAIVAgAAAB0CAAAA&ct_cookie_present=false&ocp_id=UZh-YJbwItKQgAf5rb5o&sscte=1&crd=
```

**https://www.econda-monitor.de/l/ (9)**

source: cebit.de

```
https://www.econda-monitor.de/l/00002971/t/3e7fd93a-50e4-35ce-a4bf-d0cc619ddf84?v=4&emrid=AXjury8E27X7z5HPiwcMd2dvdWsp3hXW&emsid=AXjury8FLzGI0l7jOEVL4sPpso1NlMjJ&emvid=AXjury8FLzGI0l7jOEVL4sPpso1NlMjJ&emnc=1&emtn=1&emhost=www.messe.de&tpct=1&d=eyJwYWdlSWQiOiJ3ZWJfNDAwODUwXzg0MzI3OSIsImNtc2lkIjoid2ViXzQwMDg1MF84NDMyNzkiLCJzaXRlaWQiOiIwMDAwMCIsImxhbmdpZCI6ImRlIiwiaW50ZXJuIjoid2ViIiwiY29udGVudCI6ImNvbnRlbnQvbWVzc2VuL2ludGVybmV0LXBvd2VyZWQtYnktY2ViaXQiLCJzb3VyY2UiOiJkaXJlY3QiLCJzd3NoIjoiODAweDYwMCIsInR6IjotMiwibnQiOjAsImVtb3NWIjoiYzUyLjciLCJzY3JvbGwiOlswLDAsODAwLDYwMCwxXX1JQg
```

**https://googleads4.g.doubleclick.net/pcs/view? (3)**

source: zum.de

```
https://googleads4.g.doubleclick.net/pcs/view?xai=AKAOjst01XvNZ9NzImWJ-aCWHs1ka4msoc6ZVsmMDps61AKlS1TC1LUHHltQYEzFZCXMaudSaJ8JyIeYu5RWoewxuR2CGRCsII4bX86I0F2XcSI4RjVgzboc&sig=Cg0ArKJSzKPzK9E7pozWEAE&cry=1&urlfix=1&omid=0&rm=1&ctpt=441&vt=11&dtpt=282&dett=3&cstd=146&cisv=r20210415.35417&adurl=
```
