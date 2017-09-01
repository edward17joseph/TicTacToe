public class Max{
     public static void main(String []args){
        int[] a= {10};
        int index=1;
        int max=a[0];
        while (a.length>index) {
          if (max<a[index]) {
            max=a[index];
            index=index+1;
          }
          else {
            index=index+1;
          };
        }
        System.out.println(max);
     }
}
