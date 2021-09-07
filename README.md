# Проблемы и пути их решения при осуществлении миграции программных продуктов на современные версии языка C

Научная статья посвящённая теме миграции кода со старых версий языка C на новые. 

# Аннотация
Миграция является актуальной задачей в разработке программного обеспечения. Необходимость миграции возникает с выходом обновлений языка, библиотек, фреймворков или более совершенных инструментальных средств. Более узкой задачей является миграция кода, то есть переход с одного языка программирования на другой. Миграция кода на актуальную версию языка позволяет избежать уязвимостей старых версий, избежать ошибок (исправленных в новых версиях языка), повысить быстродействие и эффективность работы кода. Однако, данная задача является сложной и до сих пор наблюдается дефицит соответствующих инструментальных средств, позволяющих мигрировать с одного языка на другой в автоматическом режиме или хотя бы позволяющих облегчить этот процесс[1][2]. Статья посвящена миграции кода, а именно переходу со старых версий языка С89/С99 на новые версии C11-C17/C23 и прототипированию транскомпилятора для автоматической миграции. 

**Ключевые слова:** портирование программного обеспечения, переносимость программ, миграция кода, транскомпиляторы.

# Источники

1) Migrate your legacy system to low code [Электронный ресурс].  — URL:  https://bit.ly/3mpFTgF (Дата обращения: 24.08.2021);
2) Legacy Software Migrations [Электронный ресурс]. — URL: https://bit.ly/3zer1VX (Дата обращения: 24.08.2021);
3) Common Data Migration Problems [Электронный ресурс]. — URL: https://bit.ly/3yi70MF (Дата обращения: 24.08.2021);
4) Five biggest challenges of software migration projects [Электронный ресурс]. — URL: https://bit.ly/3sGaffY (Дата обращения: 24.08.2021);
5) 3 Data Migration Challenges (And The Techniques To Solve Them) [Электронный ресурс]. — URL: https://bit.ly/3B7H3kZ (Дата обращения: 24.08.2021);
6) Seven reasons why system migrations fail — and how you can avoid  them [Электронный ресурс]. — URL: https://bit.ly/3gv0xYN (Дата обращения: 24.08.2021);
7) 4 REASONS WHY YOU SHOULD UPDATE YOUR SOFTWARE [Электронный ресурс]. — URL: https://bit.ly/3878K0T (Дата обращения: 24.08.2021);
8) Как мы перевели 10 миллионов строк кода C++ на стандарт C++14 (а потом и на C++17) [Электронный ресурс]. — URL: https://bit.ly/3mHD3Uv (Дата обращения: 24.08.2021);
9) Миграция баз данных: зачем и почему [Электронный ресурс]. — URL: https://bit.ly/3B9dGig (Дата обращения: 24.08.2021);
10) HipHop for PHP [Электронный ресурс]. — URL: https://bit.ly/2XHggNR (Дата обращения: 24.08.2021);
11) Liliana Martinez, Claudia Pereira, Liliana Favre Migration C/C++ Software to Mobile Platforms in the ADM Context // International Journal of Interactive Multimedia and Artificial Intelligence Vol. 4. — 2017. — №3. — P. 33 — 44;
12) Index | TIOBE — The Software Quality Company  [Электронный ресурс]. — URL: https://bit.ly/3mLBapt (Дата обращения: 25.08.2021);
13) PYPL PopularitY of Programming Languages Index  [Электронный ресурс]. — URL: https://bit.ly/38mf5FI (Дата обращения: 25.08.2021);
14) Top Computer Languages 2021 [Электронный ресурс]. — URL: https://bit.ly/3mLBh4n (Дата обращения: 25.08.2021);
15) The Top C Open Source Projects  [Электронный ресурс]. — URL: https://bit.ly/3zubDF0  (Дата обращения: 25.08.2021);
16)  Linux kernel source tree [Электронный ресурс]. — URL: https://bit.ly/38pvDww (Дата обращения: 25.08.2021);
17) Git Source Code Mirror [Электронный ресурс]. — URL: https://bit.ly/3mHKNWr (Дата обращения: 25.08.2021);
18) Redis  [Электронный ресурс]. — URL: https://bit.ly/38r6q54 (Дата обращения: 25.08.2021);
19) The PHP Interpreter  [Электронный ресурс]. — URL:https://bit.ly/2YaW3QT (Дата обращения: 25.08.2021);
20) Official Git mirror of the SQLite source tree  [Электронный ресурс]. — URL: https://bit.ly/3h3izBZ (Дата обращения: 25.08.2021);
21) History of C — cppreference.com [Электронный ресурс]. URL: https://bit.ly/3yjFXRs (Дата обращения: 25.08.2021);
22)  Extensions for parallel programming [Электронный ресурс]. — URL: https://bit.ly/3kmKFsy (Дата обращения: 25.08.2021);
23) Transactional Memory Support of C [Электронный ресурс]. — URL: https://bit.ly/2Wl68tz (Дата обращения: 24.08.2021);
24) C89 vs C99 [Электронный ресурс]. — URL: https://cw.fel.cvut.cz/old/_media/courses/be5b99cpl/lectures/be5b99cpl-lec10-handout-3x3.pdf (Дата обращения: 24.08.2021);
25) Clarification Request Summary for C11 [Электронный ресурс]. — URL: https://bit.ly/3DojOow (Дата обращения: 24.08.2021);
26) Clarification Request Summary for C2x [Электронный ресурс]. — URL:  https://bit.ly/3zrCWQs (Дата обращения: 24.08.2021);
27) How migration legacy systems improves performance and adaptability [Электронный ресурс]. URL: https://bit.ly/2WdGhEo (Дата обращения: 24.08.2021);
28) PortAssist: Visual Analysis for Porting Large Code Bases [Электронный ресурс]. — URL: https://bit.ly/3mqY31x (Дата обращения: 17.08.2021);
29) CodeCheck Program Overview — URL: https://bit.ly/38cYvbr (Дата обращения: 17.08.2021);
30) DMS Software Reengineering Toolkit [Электронный ресрус]. — URL: https://bit.ly/3znSbtr (Дата обращения: 24.08.2021);
31) Source-to-source compiler — Wikipedia [Электронный ресурс]. — URL: https://bit.ly/3zk5T0A (Дата обращения: 24.08.2021).
