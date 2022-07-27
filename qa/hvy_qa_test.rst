Harvey QA Test Suite
====================

Main QA test suite for Harvey.

.. code:: robotframework

   *** Settings ***
   Library       OperatingSystem

   *** Variables ***

   *** Test Cases ***
   Test 1
       Import Library        test1.py
       [Documentation]       Test 1
       ${RESULT} =           test1.test1
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test1.out
       File Should Exist     test1.png

   Test 2
       Import Library        test2.py
       [Documentation]       Test 2
       ${RESULT} =           test2
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test2.out
       File Should Exist     test2.png

   Test 3
       Import Library        test3.py
       [Documentation]       Test 3
       ${RESULT} =           test3
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test3.out
       File Should Exist     test3.png

   Test 4
      Import Library        test4.py
      [Documentation]       Test 4
      ${RESULT} =           test4
      Should Be Equal       ${RESULT}     ${true}
      File Should Exist     test4.out
      File Should Exist     test4.png

   Test 18
       Import Library        test18.py
       [Documentation]       Test 18
       ${RESULT} =           test18
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test18.out
       File Should Exist     test18.png

   Test 15
       Import Library        test15.py
       [Documentation]       Test 15
       ${RESULT} =           test15
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test15.out
       File Should Exist     test15.png

   Test 17
       Import Library        test17.py
       [Documentation]       Test 17
       ${RESULT} =           test17
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test17.out
       File Should Exist     test17.png

   Test 16
       Import Library        test16.py
       [Documentation]       Test 16
       ${RESULT} =           test16
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test16.out
       File Should Exist     test16.png

   Test 5
       Import Library        test5.py
       [Documentation]       Test 5
       ${RESULT} =           test5
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test5.out
       File Should Exist     test5.png

   Test 6
       Import Library        test6.py
       [Documentation]       Test 6
       ${RESULT} =           test6
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test6.out
       File Should Exist     test6.png

   Test 7
       Import Library        test7.py
       [Documentation]       Test 7
       ${RESULT} =           test7
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test7.out
       File Should Exist     test7.png

   Test 8
       Import Library        test8.py
       [Documentation]       Test 8
       ${RESULT} =           test8
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test8.out
       File Should Exist     test8.png

   #Test 9
   #    Import Library        test9.py
   #    [Documentation]       Test 9
   #    ${RESULT} =           test9
   #    Should Be Equal       ${RESULT}     ${true}
   #    File Should Exist     test9.out
   #    File Should Exist     test9.png

   Test 10
       Import Library        test10.py
       [Documentation]       Test 10
       ${RESULT} =           test10
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test10.out
       File Should Exist     test10.png

   #Test 11
   #    Import Library        test11.py
   #    [Documentation]       Test 11
   #    ${RESULT} =           test11
   #    Should Be Equal       ${RESULT}     ${true}
   #    File Should Exist     test11.out
   #    File Should Exist     test11.png

   #Test 12
   #    Import Library        test12.py
   #    [Documentation]       Test 12
   #    ${RESULT} =           test12
   #    Should Be Equal       ${RESULT}     ${true}
   #    File Should Exist     test12.out
   #    File Should Exist     test12.png

   Test 13
       Import Library        test13.py
       [Documentation]       Test 13
       ${RESULT} =           test13
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test13.out
       File Should Exist     test13.png

   Test 14
       Import Library        test14.py
       [Documentation]       Test 14
       ${RESULT} =           test14
       Should Be Equal       ${RESULT}     ${true}
       File Should Exist     test14.out
       File Should Exist     test14.png

