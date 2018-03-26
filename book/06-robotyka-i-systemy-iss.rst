************************************
Robotyka i systemy stacji kosmicznej
************************************

Istotną częścią podstawowego szkolenia astronautów jest trening wykorzystania podstawowych urządzeń robotyki kosmicznej oraz systemów ISS. Jednakże należy zwrócić uwagę na fakt, iż planowo w 2024 Międzynarodowa Stacja Kosmiczna zostanie zdeorbitowana a wykształcenie Polskiego astronauty do tego czasu jest mało prawdopodobne. Nawet jeżeli zaistniałaby możliwość, że program ISS zostanie przedłużony, to i tak wszyskie przydziały do lotów załogowych zostaną zaplanowane z dużym wyprzedzeniem. Zważywszy na powyższy fakt w ramach porgramu polskiego astronauty proponuje się odrzucenie wszelkich tematów związanych z obsługą systemów ISS.

Z tego powodu w niniejszym rozdziale zostaną opisane jednynie technologie i systemy, które mogłyby być wykorzystane w przyszłych planowanych misjach i programach.


Systemy operacyjne i oprogramowanie wykorzystywane w kosmosie
=============================================================
Międzynarodowa Stacja Kosmiczna jest złożoną konstrukcją pobierającą 84-120 kW energii dostarczanej przez panele słoneczne o powierzchni 2,500 :math:`\m^2` i rozpiętości 65 metrów. W strukturze ISS znajduje się 12.9 km kabli elektrycznych podłączonych do 52 komputerów sterujących stacją. Oprogramowanie zarządzające tą skalą ma 3.3 mln lini kodu (część naziemna) oraz 1.8 mln linii kodu część kontrolująca stację (ang. *flight software*). W ramach szkolenia astronauci poznają system operacyjny Międzynarodowej Stacji Kosmicznej wraz z jego użytkowymi detalami :cite:`ISSTechnicalDetails`, :cite:`Parazynski2017`.

System czasu
------------
Na Międzynarodowej Stacji Kosmicznej wykorzystywana jest trefa czasowa UTC, która jest kompromisem dla Centrów Kontroli Misji zarówno w Houston jak i w Moskwie.

W misjach Księżycowych opóźnienie w komunikacji sygnału elektromagnetycznego może sięgać od 1,19 do 1,35 sekundy (średnio 1,25 sek.). Wartość ta nie wpływa znacząco na obecnie wykorzystywane systemy. Problem stanowi komunikacja z obiektami np. lecącymi na większe odległości. W rozważaniach lotów w kierunku Marsa należy uwzględnić opóźnienia rzędu od 4 do 24 minut (średnio 13 min. 48 sek.). Z tego względu przy wszelkiego rodzaju komunikacji, tj. transfer danych naukowych, danych medyczny i parametrów biometrycznych, danych EVA czy komunikacji prywatnej astronauta oraz MCC może spodziewać się komplikacji i nieporozumień co dodatkow może powodować frustrację załogi oraz syndrom przemieszczenia (ang. *displacement*), który polega na rozładowaniu emocji (zwykle wrogości) na obiektach innych niż te, które je wzbudziły. Syndrom ten jest znany w specyfice lotów kosmicznych, gdzie astronauci zwykle obwiniają MCC.

Ze względu na zupełnie inny sposób liczenia czasu na powierzchni Marsa czy Księżyca do lotów długoterminowych i między ciałami niebieskimi konieczne jest wprowadzenie systemów o innej podstawie niż sekunda ziemska tj.: Coordinated Mars Time, Mars Sol Date, Lunar Standard Time. Ponadto omówiona powinna zostać również konwersje między czasami ziemskimi a kosmicznymi.

System planowania zadań
-----------------------
Planowanie zadań jest krytycznym elementem misji i wpływa na wydajność osób pracujących w kosmosie. Na skalę złożoności procesu wpływa fakt, iż planowanie składa się z trzech poziomów zadań: długoterminowych, krótkoterminowych oraz nieokreślonych w czasie. Jednocześnie są zadania, które mają możliwość być przeniesione na inny dostępny slot czasowy oraz zadania nie posiadające takiej możliwości. Do planowania i śledzenia postępu prac wykorzystuje się system informatyczny OnBoard Station Procedure Viewing Software (OBSPV).

Plan astronautów dla misji na Marsa ze względu na brak bezpośredniej komunikacji z MCC będzie w większości zadaniowy i nieprzypisany do sztywno okreslonych slotów czasowych. Wymaga to większej koordynacji i samoorganizacji pracy przez astronautów. Z drugiej strony system jest elastyczniejszy i lepiej dostosowuje się do preferencji użytkownika. Istotną kwestią pozostanie odpowiedzialność za wykonane zadania oraz śledzenie postępu wykonania.

W badaniach na ISS wzięły udział urządzenia do bezdotykowego przeglądania procedur tj. Mobile Procedure Viewer (mobiPV). Urządzenie wyglądem przypomina Google Glass i pozwala na obsługę urządzeń wykorzystywanych podczas badań z jednoczesną możliwościa kontroli procedur. MobiPV obsługuje nagrywanie materiału wideo oraz audio, jego transmisję na Ziemię oraz komunikację pomiędzy PI a astronautą.

Systemy kontroli środowiskowej i podtrzymania życia
---------------------------------------------------
Najistotniejszym elementem zarówno stacji kosmicznej jak i habitatu jest system kontroli środowiskowej i podtrzymania życia (ang. *ECLSS - Environmental Control and Life Support System*). W ramach elementów sterowanych przez system można wymienić:

- kontrola temperatury,
- kontrola wilgotności powietrza,
- kontrola parametrów i składu atmosfery,
- monitoring poziomu CO2,
- monitoring parametrów atmosfery z uwzględnieniem przesunięć czasowych,
- wizualizacja parametrów stanu habitatu,
- monitoring zużycia wody (szara, żółta, zielona, niebieska),
- zastosowanie algorytmów uczenia maszynowego w optymalizacji zużycia wody,
- zarządzanie odpadami ciekłymi,
- zarządzanie odpadami stałymi,
- kontrola oświetlenia.

System ECLSS jest podstawowym systemem każdego statku kosmicznego i stacji.

.. figure:: ../img/spacestation-iss-eclss.png
    :name: spacestation-iss-eclss
    :scale: 33%
    :align: center

    System Systemy kontroli środowiskowej i podtrzymania życia na ISS. Źródło: Wikipedia

Moduł badań naukowych i obsługi danych
--------------------------------------
Badania naukowe są głównym powodem ekploracji kosmosu. System wspierający składowanie i obróbkę danych jest więc niezwykle istotnym elementem całości. Dane, które znajdują się w systemie można podzielić na dwie kategorie: dane zbierane automatycznie oraz dane wprowazane przez astronautów. W tym celu konieczne jest zaprojektowanie odpowiedniego interfejsu.

Oprogramowanie sterujące badaniami naukowymi ma wpływ na monitoring, kontrolę parametrów środowiska w trakcie badania, informację na temat stanu urządzeń technicznych. Dla eksploracji powierzchni ciał niebieskich należy wzbogacić oporogramowanie o funkcje analizy danych geologicznych, astrobiologicznych oraz geofizycznych.

Ponadto jeżeli oprogramowanie ma być wykorzystywane do wsparcia załogi, konieczna jest również analiza danych psychologicznych i socjodynamicznych. Pozwoli to na reagowanie na wcześniejszym etapie na nieprawidłowości w zachowaniu i aktywności astronauty.

Wsparcie medyczne w długotrwałych lotach kosmicznych jest niezwykle istotnym elementem. W tym celu system musi pomóc w ewaluacji stanu astronauty i diagnozie wszelkich chorób. W tym celu można zastosować algorytmy uczenia maszynowego wykrywające anomalie w napływających danych biometrycznych oraz medycznych jak również systemy eksperckie pozwalające na wsparcie diagnozy.

Dane te mogą posłużyć również do planowania aktywności astronautów, dostosowania intensywności i długości ćwiczeń jak również w optymalizacji poruszania się załogi.

System śledzenia inwentarza
---------------------------
Ogromna objętość i złożoność stacji kosmicznej sprzyja możliwości gubienia przedmiotów i narzędzi. Ponadto międzynarodowy i rotacyjny charakter załóg powoduje, że konieczne stało się stworzenie systemu śledzenia inwentarza. Każdy przedmiot wykorzystywany na ISS ma unikalny identyfikator, dzięki czemu astronauta, który go używa może w szybki sposób oznaczyć ten fakt skanując jego kod kreskowy.

Informacje na temat położenia przedmiotów, daty ważności (w przypadku lekarstw i pożywienia) są przetrzymywane w systemie. Prowadzenie elektronicznego inwentarza pozwala na monitorowanie poziomu zapasów zasobów zużywających się (ang. *consumables*).

Dobrze użyty system potrafi śledzić kaloryczność oraz wartości odżywcze pokarmów przyjmowanych przez załogę co jest konieczne przy utrzymywaniu zbalansowanej diety zawierającej minerały spowalniające niekorzystne czynniki działania w środowisku mikrograwitacji.

System ponadto pozwala na monitorowanie stanu przedmiotów, ich uszkodzeń oraz prowadzenie dziennika napraw.

Komunikacja
-----------
- Dzienniki osobiste
- Dzienniki audio i wideo
- Zastosowanie algorytmów uczenia maszynowego w analizie intencji tekstów, materiałów audio oraz wideo

System wsparcia EVA
-------------------
- Mapowanie terenu i odwzorowanie kartograficzne
- Planowanie spacerów kosmicznych i planetarnych
- Monitoring pozycji astronautów w czasie rzeczywistym
- Strumieniowanie danych audiowizualnych
- Parametry biomedyczne skafandra
- Wsparcie dla sytuacji awaryjnych
- Wsparcie współpracy z systemami robotycznymi
- Systemy wsparcia rozszerzonej rzeczywistości i wyświetlania procedur operacyjnych
- Zmiana celów w trakcie trwania EVA
- Odprawa i rozliczanie załóg

Systemy wsparcia robotycznego
=============================


.. figure:: ../img/iss-robotics-controller.jpg
    :name: figure-iss-robotics-controller
    :scale: 33%
    :align: center

    Astronautka NASA Christina M. Hammock podczas ćwiczeń systemów robotycznych. Źródło: NASA/JSC

Manipulator SSRMS Canadarm 2
----------------------------

.. todo:: The MSS is composed of three components - the Space Station Remote Manipulator System (SSRMS), known as Canadarm2, the Mobile Remote Servicer Base System (MBS) and the Special Purpose Dexterous Manipulator (SPDM, also known as Dextre or Canada hand). The system can move along rails on the Integrated Truss Structure on top of the US provided Mobile Transporter cart which hosts the MRS Base System. The system's control software was written in the Ada 95 programming language.[http://www.adacore.com/uploads/customers/CaseStudy_SpaceArm.pdf]

​
50 feet length (old arm?)
Three jointed shoulder
Elbow
Three jointed wrist
Able to change base location
7 joints 540 degrees rotation
Force moment sensors for Force feedback
Advanced automatic vision system
Basic Collision avoidance system
250.000 lbs. payload handling


Urządzenie Mobile Remote Servicer Base System
---------------------------------------------


Manipulator Special Purpose Dexterous Manipulator
-------------------------------------------------

Wykorzystanie systemów robotycznych
===================================

Dokowanie statków kosmicznych
-----------------------------
.. todo::
    - Za pomocą Canadaarm2
    - ATV
    - Dragon
    - Progress

Asystowanie przy spacerach kosmicznych
--------------------------------------

Symulacja przechwytywania pojazdów kosmicznych na orbicie
=========================================================

Sterowanie robotami na Ziemi z orbity
======================================

Urządzenia wirtualnej rzeczywistości
======================================


Analiza szkolenia robotycznego i systemów ISS w kontekście celu pracy
=====================================================================
Ze względu na brak trenażerów systemów ISS, jego wewnętrznej i zewnętrznej części jak również na chwilę obecną brak basenu nadającego się do prowadzenia szkolenia z EVA niemożliwe jest odtworzenie tych elementów szkolenia. Jednakże należy zwrócić uwagę na fakt, iż planowo w 2024 Międzynarodowa Stacja Kosmiczna zostanie zdeorbitowana a wykształcenie polskiego astronauty do tego czasu jest mało prawdopodobne. Nawet jeżeli zaistniałaby możliwość, że program ISS zostanie przedłużony, to i tak wszyskie przydziały do lotów załogowych zostaną zaplanowane z dużym wyprzedzeniem. Zważywszy na powyższy fakt w ramach porgramu polskiego astronauty proponuje się odrzucenie wszelkich tematów związanych z obsługą systemów ISS.

Szkolenie z wykorzystywania i utrzymywania ISS jest jednym z najbardziej czasochłonnych oraz zasobochłonnych aspektów szkolenia astronautów. Proponowane rozwiązanie wykluczenia powyższych elementów ze szkolenia pozwoli nie tylko na optymalizację kosztów, jak również zwiększy możliwość procentowego udziału w szkoleniu w Polsce.

Obecnie planowane są misje na Księżyc, Mars oraz asteroidy i inne ciała o niewielkim przyciąganiu grawitacyjnym. Autor pracy sugeruje aby wykorzystać nowatorskie badania i unikalną infrastrukturę aby rozwinąć program szkolenia przygotowujący do lotów na inne ciała niebieskie. Dzięki habitatowi Lunares Polska nie tylko jest w stanie szkolić astronautów, ale również wieść prym w nowej klasie treningów.
