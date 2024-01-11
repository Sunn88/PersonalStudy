package mentorJava.ch03연산자;

class I{}
class J extends I{}


public class OperPrac {

	public static void main(String[] args) {
		
		int a = 1;
		System.out.println(a);
		
		a++; //a의 값을 1 증가
		System.out.println(a); //증가되었으므로 2
		System.out.println(++a); //증가시킨 다음 출력하므로 3
		System.out.println(a++); //3을 출력 후 증가
		System.out.println(a); //현재는 4
		
		System.out.println("================================");
		
		int b = 10;
		int c = 20;
		int d = 30;
		System.out.println(b < c); //true
		System.out.println(b > c); //false
		System.out.println(b + c <= d); //true
		System.out.println(b + c >= d); //true
		
		System.out.println("================================");
		
		double e = 3.14;
		double f = 5.14;
		System.out.println(e == f); //false
		System.out.println(e != f); //true
		
		String c1 = "Hello JAVA!";
		System.out.println(c1.equals("Hello java!")); //false
		System.out.println(c1.equals("Hello JAVA!")); //true
		
		System.out.println("================================");
		
		int age = 17;
		System.out.println(age > 19 ? "성인입니다." : "청소년입니다.");

		System.out.println("================================");
		
		int g = 3;
		int h = 5;
		
		h = g; //순수 대입
		System.out.println(h); //3
		
		g += 1;
		System.out.println(g); //4
		g /= 2;
		System.out.println(g); //2
		g += g;
		System.out.println(g); //4

		System.out.println("================================");
		
		I i = new I();
		J j = new J();
		
		System.out.println("i instanseof I : " + (i instanceof I)); //true
		System.out.println("j instanseof I : " + (j instanceof I)); //true
		System.out.println("i instanseof J : " + (i instanceof J)); //false
		System.out.println("j instanseof J : " + (j instanceof J)); //true
		
	}
}
