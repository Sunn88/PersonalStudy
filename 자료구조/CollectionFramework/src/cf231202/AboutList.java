package cf231202;

import java.util.*;

public class AboutList {

	
//	T는 객체 타입을 의미하며 기본적으로 Integer, String, Double, Long 같은 Wrapper Class부터 사용자 정의 객체까지 가능하다.
//	ex) LinkedList<Integer> list = new LinkedList<>();
//	primitive type은 불가능하다.
	
	 
	// 방법 1
	ArrayList<T> arraylist = new ArrayList<>();
	LinkedList<T> linkedlist = new LinkedList<>();
	Vector<T> vector = new Vector<>();
	Stack<T> stack = new Stack<>();
	 
	// 방법 2
	List<T> arraylist = new ArrayList<>();
	List<T> linkedlist = new LinkedList<>();
	List<T> vector = new Vector<>();
	List<T> stack = new Stack<>();
	 
	// Stack은 Vector를 상속하기 때문에 아래와 같이 생성할 수 있다.
	Vector<T> stack = new Stack<>();
	
}
