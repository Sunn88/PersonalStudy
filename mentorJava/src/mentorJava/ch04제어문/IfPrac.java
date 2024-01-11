package mentorJava.ch04제어문;

import java.util.Scanner;

public class IfPrac {

	public static void main(String[] args) {
		
		int a = 5;
		if(a > 3) {
			System.out.println("a는 3보다 큽니다.");
		}
		System.out.println("검사가 끝났습니다.");
		
		System.out.println("================================");
		
		int age = 15;
		if(age > 19) {
			System.out.println("성인입니다. 성인 요금이 적용됩니다.");
		}else {
			System.out.println("청소년입니다. 청소년 요금이 적용됩니다.");
		}
		System.out.println("결제를 진행해주세요.");
		
		System.out.println("================================");
		
		Scanner input = new Scanner(System.in);
		age = input.nextInt();
		
	}
}
