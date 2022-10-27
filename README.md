Project ADML : A Million Star-Galaxy Image Dataset
---------------------------------------------------------

![A Million Star-Galaxy Image Dataset](https://raw.githubusercontent.com/PlutoMingyu/A-Million-Star-Galaxy-Image-Dataset/master/0.%20for%20GuideBook/A%20Million%20Star-Galaxy%20Dataset%20Logo_Dark.png)

### Project ADML : 'A Million Star-Galaxy Image Dataset'   
#### The dataset consists of one million images and labels.
#### Number of Star Data : 630,000 / Number of Galaxy Data : 370,000   

--------------------------------------------------------------------------------   

#### 'A Million Star-Galaxy Image Dataset'은 100만 개의 데이터로 구성되어 있습니다.
#### 별 데이터 : 630,000개, 은하 데이터 : 370,000개   

--------------------------------------------------------------------------------

> A Million Star-Galaxy Image Dataset에 대한 설명은 영어와 한글로 구성되어 있습니다.   
> [**1. A Million Star-Galaxy Image Dataset을 소개합니다**](https://github.com/PlutoMingyu/A-Million-Star-Galaxy-Image-Dataset#1-a-million-star-galaxy-image-dataset%EC%9D%84-%EC%86%8C%EA%B0%9C%ED%95%A9%EB%8B%88%EB%8B%A4) : 한글 버전을 읽으려면 링크를 클릭하세요.   

--------------------------------------------------------------------------------

# 1. Introduction
A Million Star-Galaxy Image Dataset is design and build to improve the performance of the Star-Galaxy Classification Problem (SGCP).
SGCP is a traditional problem in astronomy, which is difficult to distinguish in images due to the geometrical similarity between stars and galaxies.   
Advances in observing equipment and technology have allowed us to see darker objects, which means is that stars and galaxies images become darker and smaller.
Therefore, SGCP was still considered a valid problem to be solved, and the first step toward this was to design and build a Star-Galaxy Image Dataset.   

# 2. Design of A Million Star-Galaxy Image Dataset   


--------------------------------------------------------------------------------

> ADML의 한글 버전 가이드입니다.
# 1. A Million Star-Galaxy Image Dataset을 소개합니다
별-은하 이미지 데이터세트은 별-은하 분류문제(SGCP, Star-Galaxy Classification Problem)의 성능 개선을 위해 설계 및 구축했습니다.   
SGCP는 별과 은하의 형상적 유사함으로 인해 이미지에서 구분이 어려워 발생하는 천문학 분야에서 오랜기간 고민해오고 있는 문제 중 하나입니다. 관측 장비와 기술의 발전에 따라 우리는 더 어두운 대상을 볼 수 있게 되었고, 이는 구별해야하는 별과 은하의 크기가 보다 작아지고 어두워짐을 의미합니다.   
따라서, SGCP는 여전히 유효한 해결해야할 문제라고 생각하게 되었고 이를 위한 첫번째 계단으로 별-은하 이미지 데이터세트을 설계 및 구축하게 되었습니다.   

# 2. 별-은하 이미지 데이터세트 설계   
### 데이터는 JPEG 이미지와 JSON 형식의 메타데이터 파일로 구성됩니다.
## 2-1. 데이터의 출처   
데이터세트를 구성하는 이미지 및 메타 데이터는 [**SDSS DR17**](https://www.sdss.org/)(Sloan Digital Sky Survey)의 DR(Data Release) 17 데이터를 사용했습니다.   

<img src="https://www.sdss.org/wp-content/uploads/2014/11/SDSS_telescope_new.jpg" width="65%" height="65%" title="%(비율) 크기 설정" alt="Sloan Foundation 2.5m Telescope"></img>   

#### Sloan Foundation 2.5m Telescope

SDSS는 관측 가능한 우주 전체에 대한 광범위한 조사를 통해 이미지와 스펙트럼 등의 데이터를 공개 및 제공합니다.   

## 2-2. 이미지 데이터 정보
### - 크기 및 형식 : 512 × 512 × 3 (RGB) JPEG   
SDSS에서 g, r, i 파장의 데이터를 합성 및 보정하여 제공하는 이미지를 사용합니다.   
여기서 g는 가시광선의 녹색 영역, r은 가시광선의 적색 영역, i는 적외선 영역 중 7600Å 파장입니다.   

    u : Ultra Violet, 3551Å
    g : Visual Light - Green, 4686Å
    r : Visual Light - Red, 6166Å
    i : Infra Red, 7480Å
    z : Infra Red, 8932Å   

<img src="https://www.sdss.org/wp-content/uploads/2014/11/camera_filters-300x274.jpg" width="40%" height="40%" title="%(비율) 크기 설정" alt="The SDSS-III camera filter throughput curves"></img>   

#### The SDSS-III camera filter throughput curves   

> SDSS 카메라의 정보 (필터 및 파장) : [**SDSS - Camera**](https://www.sdss.org/instruments)   

이미지의 다운로드는 적경, 적위, 스케일, 이미지 크기-가로 및 세로를 입력하여 다운로드 합니다. 다운로드한 파일의 이름은 'NoIndex_Class_ObjID.jpg' 형태로 저장됩니다.   

> SDSS에서 사용하는 장비(망원경, 카메라, 필터)에 대한 정보 : [**SDSS - Telescopes and Instruments**](https://www.sdss.org/instruments)   
> SDSS에서 다운로드한 JEPG 이미지에 대한 정보 : [**SDSS - JPEG Images on SkyServer**](https://www.sdss.org/dr17/imaging/jpg-images-on-skyserver/)   

<img src="https://github.com/PlutoMingyu/A-Million-Star-Galaxy-Image-Dataset/blob/master/0.%20for%20GuideBook/GALAXY_1237667254549282989%20Image%20Data.png" width="65%" height="65%" title="%(비율) 크기 설정" alt="GALAXY_1237667254549282989 Image Data"></img>

<img src="https://github.com/PlutoMingyu/A-Million-Star-Galaxy-Image-Dataset/blob/master/0.%20for%20GuideBook/Scale%20comparison%20of%20GALAXY_1237665427567804598%20image%20data.png" width="65%" height="65%" title="%(비율) 크기 설정" alt="Scale comparison of GALAXY_1237665427567804598"></img>   


# 2. 별-은하 이미지 데이터세트 구축   

<img src="https://github.com/PlutoMingyu/A-Million-Star-Galaxy-Image-Dataset/blob/master/0.%20for%20GuideBook/Dataset%20building%20process.png" width="65%" height="65%" title="%(비율) 크기 설정" alt="Dataset building process"></img>   


# 3. 별-은하 이미지 데이터세트 성능 검증   

<img src="https://github.com/PlutoMingyu/A-Million-Star-Galaxy-Image-Dataset/blob/master/0.%20for%20GuideBook/The%20challenge%20of%20star-galaxy%20image%20classification.png" width="65%" height="65%" title="The challenge of star-galaxy image classification" alt="The challenge of star-galaxy image classification"></img>