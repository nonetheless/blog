JUnit5
=============
[参考](https://www.ibm.com/developerworks/cn/java/j-introducing-junit5-part1-jupiter-api/index.html)
### 新的结构
新的Junit的整体架构不再是以前的一个大的jar包了，通过将JUnit Jupiter分离开来支持更多的测试框架
![Junit](https://www.ibm.com/developerworks/cn/java/j-introducing-junit5-part1-jupiter-api/Figure-1.png)
可以轻松定义不同的测试框架。只要一个框架实现了 TestEngine 接口，就可以将它插入任何支持 junit-platform-engine 和 junit-platform-launcher API 的工具中
### 新的特性
新的Junit支持assertAll的方法可以批量执行判断，而且会全部执行完，不会在第一个断言失败后就停止判断。
---------------------------------------
    import static org.junit.jupiter.api.Assertions.assertAll;
    @Test
    @DisplayName("Dummy test")
    void dummyTest() {
        int expected = 4;
        int actual = 2 + 2;
        Object nullValue = null;
        assertAll(
            "Assert All of these",
            () -> assertEquals(expected, actual, "INCONCEIVABLE!"),
            () -> assertFalse(nullValue != null),
            () -> assertNull(nullValue),
            () -> assertNotNull("A String", "INCONCEIVABLE!"),
            () -> assertTrue(nullValue == null)
        );
     }
---------------------------------------
支持assertThrow，来对异常情况的用例做单元测试
---------------------------------------
    import static org.junit.jupiter.api.Assertions.assertThrows;
    import static org.junit.jupiter.api.Assertions.assertEquals;
    @Test()
    @DisplayName("Empty argument")
    public void testAdd_ZeroOperands_EmptyArgument() {
        long[] numbersToSum = {};
        assertThrows(IllegalArgumentException.class, () -> classUnderTest.add(numbersToSum);
     }
---------------------------------------        
支持assume对前置条件判断
---------------------------------------
    @Test
    @DisplayName("This test is only run on Fridays")
    public void testAdd_OnlyOnFriday() {
        LocalDateTime ldt = LocalDateTime.now();
        assumeTrue(ldt.getDayOfWeek().getValue() == 5);
        //Remainder of test (only executed if assumption holds)
        }
---------------------------------------   
    
