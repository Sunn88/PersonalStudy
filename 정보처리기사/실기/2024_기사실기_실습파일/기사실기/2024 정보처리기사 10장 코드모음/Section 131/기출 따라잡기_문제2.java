public class Test {
	public static void main(String[] args) {
		try {
			int a = 32, b = 0;
			double c = a / b;
			System.out.print('A');
		}
		catch (ArithmeticException e) {
			System.out.print('B');
		}
		catch (NumberFormatException e) {
			System.out.print('C');
		}
		catch (Exception e) {
			System.out.print('D');
		}
	}
}