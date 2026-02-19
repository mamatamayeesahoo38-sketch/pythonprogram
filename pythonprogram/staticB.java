class staticB
{
    static int data;
    static void show()
    {
        data=10;
        System.out.println(data); //10
    }
}
class Test
{
    public static void main(String arg[])
    {
          System.out.println(staticB.data);
          staticB.show();
          System.out.println(staticB.data);

    }
}
