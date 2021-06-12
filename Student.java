import java.util.Scanner;
import java.io.*;



private class demo extends Student {
	int demo1()
}

demo y[] = new demo[100];

public class Student {
	String usn;
	String name;
	String branch;
	Long phone;
	void read() {
        Scanner in = new Scanner(System.in);

		System.out.println("Enter USN:");
		usn = in.nextLine();

		System.out.println("Enter Name:");
		name = in.nextLine();

		System.out.println("Enter Branch:");
		branch = in.nextLine();

		System.out.println("Enter Phone Number:");
		phone = in.nextLong();
	}

	void print() {
	System.out.println(usn + "\t| " + name + "\t| " + branch + "\t| " + phone);
	System.out.println("---------------------------------------------\n");
	}
/*--------------*/
	public static void main(String args[]) {
		int i,n;
		Student s[]= new Student[100];
		Student x[] = new Student[100];
		Scanner in = new Scanner(System.in);

		System.out.println("How Many Students Details you want to Enter:");
		n = in.nextInt();

		System.out.println("Enter details of " + n + " students\n");
		for(i = 0; i<n; i++) {
			s[i]= new Student();
			s[i].read();
		}

		System.out.println("****STUDENTS DETAILS ARE****\n");
		System.out.println("USN \t\t| NAME \t\t| BRANCH \t\t| PHONE |\n");

		for(i = 0; i<n; i++) {
			s[i].print();
		}
	}
}