import java.util.Scanner;

class Node{
    int data;
    Node next;
    Node head;
    int data(){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the value : ");
        int data = input.nextInt();
        return data;
    }
    int position(){
        Scanner pos = new Scanner(System.in);
        System.out.print("Enter the position : ");
        int position = pos.nextInt();
        return position;
    }
    void insertAtBegin(){
        Node newNode = new Node();
        newNode.data = data();
        newNode.next = null;
        if (head == null){
            head = newNode;
        }
        else {
            newNode.next = head;
            head = newNode;
        }
    }
    void insertAtEnd(){
        Node newNode = new Node();
        newNode.data = data();
        newNode.next = null;
        if (head==null){
            head = newNode;
        }
        else {
            Node temp = head;
            while (temp.next != null){
                temp=temp.next;
            }
            temp.next = newNode;
        }
    }
    void insertAtPosition(){
        Node newNode = new Node();
        newNode.data = data();
        Node temp = head;
        int pos = position();
        if (pos == 0 ){
            insertAtBegin();
        }
        else {
            for (int i=1; i<pos; i++){
                temp = temp.next;
                if (temp == null){
                    System.out.println("invalid input");
                }
            }
        }
        newNode.next = temp.next;
        temp.next = newNode;
    }
    void deleteAtBegin(){
        if (head == null){
            System.out.println("List is empty");
        }
        else {
            head = head.next;
        }
    }
    void deleteAtPosition(){
        Node temp = head;
        Node pre = null;
        int pos = position();
        if (pos==0){
            deleteAtBegin();
        }
        for (int i=1; i<=pos; i++){
            if (temp==null){
                System.out.println("invalid input");
            }
            pre = temp;
            temp = temp.next;
        }
        if (temp==null){
            System.out.println("invalid input");
        }
        pre.next = temp.next;
    }
    void displayList(){
        System.out.println("The list is ");
        Node temp = head;
        while (temp != null){
            System.out.print(temp.data+" ");
            temp = temp.next;
        }
        System.out.println();
    }
}
public class SingleLinkedList extends Node{
    public static void main(String[] args) {
        SingleLinkedList SLL = new SingleLinkedList();
        Scanner input = new Scanner(System.in);
        int exit=1;
        while (exit==1){
            System.out.println("1. Insert at Begin ");
            System.out.println("2. Insert at End ");
            System.out.println("3. Insert at Position ");
            System.out.println("4. Delete at Begin ");
            System.out.println("5. Delete at Position ");
            System.out.println("6. Display List");
            System.out.println("7. Exit");
            System.out.print("Enter the choise preference : ");
            int choise = input.nextInt();
            if (choise==1){
                SLL.insertAtBegin();
            } else if (choise==2) {
                SLL.insertAtEnd();
            } else if (choise==3) {
                SLL.insertAtPosition();
            } else if (choise==4) {
                SLL.deleteAtBegin();
            } else if (choise==5) {
                SLL.deleteAtPosition();
            } else if (choise==6) {
                SLL.displayList();
            } else if (choise==7) {
                System.out.println("Do you want to display the list finally");
                System.out.print("If yes, press 'Y' or else press any other key   ");
                String out = input.next();
                if (out.equals("y") || out.equals("Y")){
                    SLL.displayList();
                    System.out.println("\nProgram has been terminated!\n\t- YoN Coding");
                }
                else {
                    System.out.println("Program has been terminated!\n\t- YoN Coding");
                }
                exit = 0;
            } else {
                System.out.println("Enter the valid choise preference!");
            }
        }
    }
}