import java.util.Scanner;

class DoublyMethods {
    int data;
    DoublyMethods prev;
    DoublyMethods next;
    DoublyMethods head = null;
    DoublyMethods tail = null;
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
    void insertAtBegin() {
        int data = data();
        DoublyMethods newDubNode = new DoublyMethods();
        newDubNode.data = data;
        if (head == null) {
            newDubNode.next=null;
            newDubNode.prev=null;
            head = newDubNode;
            tail=newDubNode;
        }
        else {
            newDubNode.next=head;
            newDubNode.prev=null;
            head.prev=newDubNode;
            head=newDubNode;
        }
    }

    void insertAtEnd() {
        int data = data();
        DoublyMethods newDubNode = new DoublyMethods();
        newDubNode.data = data;
        newDubNode.next = null;
        newDubNode.prev = null;
        if (head == null) {
            newDubNode.prev = null;
            head = newDubNode;
            return;
        }
        DoublyMethods temp = head;
        while (temp.next != null) {
            temp = temp.next;
        }
        temp.next = newDubNode;
        newDubNode.prev = temp;
        tail=newDubNode;
    }
    void insertAtPos() {
        int data = data();
        int pos = position();
        if (pos == 0) {
            insertAtBegin();
            return;
        }
        DoublyMethods newDubNode = new DoublyMethods();
        newDubNode.data = data;
        DoublyMethods temp = head;
        for (int i = 1; i < pos; i++) { // jump to prev node
            temp = temp.next;
        }
        if (temp == null) {
            System.out.println("Invalid input");
            return;
        }
        newDubNode.next = temp.next;
        newDubNode.prev = temp;
        temp.next.prev=newDubNode;
        temp.next = newDubNode;
    }
    void deleteAtBegin() {
        if (head == null) {
            System.out.println("list is empty");
            return;
        }
        head = head.next;
        if (head != null) {
            head.prev = null;
        }
    }
    void deleteAtPos() {
        int pos = position();
        if (head == null) {
            System.out.println("list is empty");
            return;
        }
        if (pos == 0) {
            deleteAtBegin();
            return;
        }
        DoublyMethods temp = head;
        DoublyMethods prev=null;
        for (int i = 1; i <= pos; i++) {
            if (temp == null) {
                System.out.println("Invalid input");
                return;
            }
            prev=temp;
            temp = temp.next;
        }
        prev.next=temp.next;
        temp.next.prev=prev;
    }
    void displayList() {
        if(head==null) {
            System.out.println("list is empty");
        }
        DoublyMethods temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next; //jump
        }
        System.out.println();
    }
    void displayRevList() {
        DoublyMethods temp = tail;// Start from the tail
        while(temp!=null) {
            System.out.print(temp.data + " ");
            temp = temp.prev; // Move to the previous node
        }
        System.out.println();
    }
}

public class DoublyLinkedList extends DoublyMethods {
    public static void main(String[] args) {
        DoublyLinkedList DLL = new DoublyLinkedList();
        Scanner input = new Scanner(System.in);
        int exit=1;
        while (exit==1){
            System.out.println("1. Insert at Begin ");
            System.out.println("2. Insert at End ");
            System.out.println("3. Insert at Position ");
            System.out.println("4. Delete at Begin ");
            System.out.println("5. Delete at Position ");
            System.out.println("6. Display List");
            System.out.println("7. Display List (Reversed)");
            System.out.println("8. Exit");
            System.out.print("Enter the choise preference : ");
            int choise = input.nextInt();
            if (choise==1){
                DLL.insertAtBegin();
            } else if (choise==2) {
                DLL.insertAtEnd();
            } else if (choise==3) {
                DLL.insertAtPos();
            } else if (choise==4) {
                DLL.deleteAtBegin();
            } else if (choise==5) {
                DLL.deleteAtPos();
            } else if (choise==6) {
                DLL.displayList();
            } else if (choise==7) {
                DLL.displayRevList();
            } else if (choise==8) {
                System.out.println("Do you want to display the list finally");
                System.out.print("If yes, press 'Y' or else press any other key   ");
                String out = input.next();
                if (out.equals("y") || out.equals("Y")){
                    DLL.displayList();
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