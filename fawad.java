//Stack

package stack;
import java.util.Scanner;

public class StackImplementation<T> {
    T[] arr;
    int top = -1;
    Scanner s1 = new Scanner(System.in);

    StackImplementation(int size) {
        arr = (T[]) new Object[size];
    }

    void push(T item) {
        if (top >= arr.length - 1) {
            System.out.println("Overflow Error.");
        } else {
            top++;
            arr[top] = item;
        }
    }

    void pop() {
        if (top >= 0) {
            top--;
        } else {
            System.out.println("Underflow Error.");
        }
    }

    boolean checkStackEmpty() {
        if (top == -1) {
            return true;
        } else {
            return false;
        }
    }

    T peek() {
        if (top < 0){
            return null;
        }else {
            return arr[top];
        }
    }

    void displayElements() {
        System.out.print("[");
        for (int i = 0; i <= top; i++) {
            System.out.print(arr[i]);
            if (i != top) {
                System.out.print(",");
            }
        }
        System.out.print("]");
    }

}















//queue


package queue;

public class QueueImplementation <T>{

    private T[] arr;
    private int rear = -1;
    private int front = -1;

    QueueImplementation(int sizeOfQueue){
        arr = (T[]) new Object[sizeOfQueue];
    }

    void enqueue(T item){
        if(rear == -1 && front == -1){
            rear = 0;
            front = 0;
            arr[rear] = item;
        }else if(rear == arr.length - 1){
            System.out.println("Overflow Error");
        }else{
            rear++;
            arr[rear] = item;
        }
    }

    void dequeue(){
        if(rear == -1 && front == -1){
            System.out.println("Underflow Error");
        } else if (front == rear) {
            front = -1;
            rear = -1;
        }else {
            front++;
        }
    }

    T front(){
        if(rear != -1 && front != -1) {
            return arr[front];
        }else{
            return null;
        }
    }

    T rear(){
        if(rear != -1 && front != -1) {
            return arr[rear];
        }else{
            return null;
        }
    }

    int sizeOfQueue(){
        if (rear != -1 && front != -1) {
            return (rear - front) + 1;
        }else{
            return 0;
        }
    }

    void displayQueue(){
        System.out.print("[");
        if(rear != -1 && front != -1) {
            for (int i = front; i <= rear; i++) {
                System.out.print(arr[i]);
                if (i != rear) {
                    System.out.print(",");
                }
            }
        }
        System.out.print("]");
    }

    boolean isEmpty(){
        return rear == -1 && front == -1;
    }

}





















package postfix;
import java.util.Objects;
import java.util.Stack;

public class Postfix {
    String expression;

    Postfix(String expression) {
        this.expression = expression;
    }

    String findPostfix() {
        expression = expression + ")";
        String solution = "";
        Stack<String> stack = new Stack<>();
        stack.push("(");
        for (int i = 0; i < expression.length(); i++) {
            char currentCharacter = expression.charAt(i);
            if (currentCharacter == 'A' || currentCharacter == 'B' || currentCharacter == 'C' || currentCharacter == 'D' || currentCharacter == 'E' || currentCharacter == 'F' || currentCharacter == 'G' || currentCharacter == 'H') {
                solution = solution + currentCharacter;
            } else if (currentCharacter == '(') {
                stack.push(String.valueOf(currentCharacter));
            } else if (currentCharacter == '+' || currentCharacter == '-') {
                if (Objects.equals(stack.peek(), "-") || Objects.equals(stack.peek(), "+") || Objects.equals(stack.peek(), "/") || Objects.equals(stack.peek(), "*") || Objects.equals(stack.peek(), "^")) {
                    solution += stack.pop();
                    stack.push(String.valueOf(currentCharacter));
                } else {
                    stack.push(String.valueOf(currentCharacter));
                }
            } else if (currentCharacter == '*' || currentCharacter == '/') {
                if (Objects.equals(stack.peek(), "/") || Objects.equals(stack.peek(), "*") || Objects.equals(stack.peek(), "^")
                ) {
                    solution += stack.pop();
                    stack.push(String.valueOf(currentCharacter));
                } else {
                    stack.push(String.valueOf(currentCharacter));
                }
            } else if (currentCharacter == '^') {
                stack.push(String.valueOf(currentCharacter));
            } else if (currentCharacter == ')') {
                while (true) {
                    if (!Objects.equals(stack.peek(), "(")) {
                        solution += stack.pop();
                    } else {
                        stack.pop();
                        break;
                    }
                }
            }
        }

        return solution;
    }
}



























package circularqueue;

public class CircularQueue<T> {

    private T[] arr;
    private int front;
    private int rear;

    public CircularQueue(int size) {
        arr = (T[]) new Object[size];
        front = -1;
        rear = -1;
    }

    public boolean isEmpty() {
        return front == -1;
    }

    public boolean isFull() {
        return (rear + 1) % arr.length == front;
    }

    public void enqueue(T item) {

        if (isFull()) {
            System.out.println("Overflow Error");
            return;
        }

        if (isEmpty()) {
            front = rear = 0;
        } else {
            rear = (rear + 1) % arr.length;
        }

        arr[rear] = item;
    }

    public T dequeue() {

        if (isEmpty()) {
            System.out.println("Underflow Error");
            return null;
        }

        T removed = arr[front];

        if (front == rear) {
            front = rear = -1;
        } else {
            front = (front + 1) % arr.length;
        }

        return removed;
    }

    public T front() {
        return isEmpty() ? null : arr[front];
    }

    public T rear() {
        return isEmpty() ? null : arr[rear];
    }

    public void display() {

        if (isEmpty()) {
            System.out.println("[]");
            return;
        }

        System.out.print("[");

        int i = front;

        while (true) {

            System.out.print(arr[i]);

            if (i == rear) {
                break;
            }

            System.out.print(", ");

            i = (i + 1) % arr.length;
        }

        System.out.println("]");
    }
}



























package deque;
public class CircularDequeInputRestrict<T> {

    private T[] arr;
    private int front = -1;
    private int rear  = -1;
    private int size;

    CircularDequeInputRestrict(int size) {
        this.size = size;
        arr = (T[]) new Object[size];
    }

    boolean isEmpty() {
        return front == -1;
    }

    boolean isFull() {
        return (rear + 1) % size == front;
    }

    void enqueueRear(T item) {
        if (isFull()) {
            System.out.println("Overflow Error: Circular Deque is full.");
            return;
        }
        if (isEmpty()) {
            front = 0;
            rear  = 0;
        } else {
            rear = (rear + 1) % size;
        }
        arr[rear] = item;
    }

    T dequeueFront() {
        if (isEmpty()) {
            System.out.println("Underflow Error: Circular Deque is empty.");
            return null;
        }
        T item = arr[front];
        if (front == rear) {
            front = -1;
            rear  = -1;
        } else {
            front = (front + 1) % size;
        }
        return item;
    }

    T dequeueRear() {
        if (isEmpty()) {
            System.out.println("Underflow Error: Circular Deque is empty.");
            return null;
        }
        T item = arr[rear];
        if (front == rear) {
            front = -1;
            rear  = -1;
        } else {
            rear = (rear - 1 + size) % size;
        }
        return item;
    }

    T peekFront() {
        return isEmpty() ? null : arr[front];
    }

    T peekRear() {
        return isEmpty() ? null : arr[rear];
    }

    void display() {
        if (isEmpty()) {
            System.out.println("[]");
            return;
        }
        System.out.print("[");
        int i = front;
        while (true) {
            System.out.print(arr[i]);
            if (i == rear) break;
            System.out.print(", ");
            i = (i + 1) % size;
        }
        System.out.println("]");
    }
}











package deque;
public class CircularDequeOutputRestrict<T> {

    private T[] arr;
    private int front = -1;
    private int rear  = -1;
    private int size;

    CircularDequeOutputRestrict(int size) {
        this.size = size;
        arr = (T[]) new Object[size];
    }

    boolean isEmpty() {
        return front == -1;
    }

    boolean isFull() {
        return (rear + 1) % size == front;
    }
    void enqueueRear(T item) {
        if (isFull()) {
            System.out.println("Overflow Error: Circular Deque is full.");
            return;
        }
        if (isEmpty()) {
            front = 0;
            rear  = 0;
        } else {
            rear = (rear + 1) % size;
        }
        arr[rear] = item;
    }

    void enqueueFront(T item) {
        if (isFull()) {
            System.out.println("Overflow Error: Circular Deque is full.");
            return;
        }
        if (isEmpty()) {
            front = 0;
            rear  = 0;
        } else {
            front = (front - 1 + size) % size;
        }
        arr[front] = item;
    }

    T dequeueFront() {
        if (isEmpty()) {
            System.out.println("Underflow Error: Circular Deque is empty.");
            return null;
        }
        T item = arr[front];
        if (front == rear) {
            front = -1;
            rear  = -1;
        } else {
            front = (front + 1) % size;
        }
        return item;
    }

    T peekFront() {
        return isEmpty() ? null : arr[front];
    }

    T peekRear() {
        return isEmpty() ? null : arr[rear];
    }

    void display() {
        if (isEmpty()) {
            System.out.println("[]");
            return;
        }
        System.out.print("[");
        int i = front;
        while (true) {
            System.out.print(arr[i]);
            if (i == rear) break;
            System.out.print(", ");
            i = (i + 1) % size;
        }
        System.out.println("]");
    }
}














package deque;
public class DequeImplementationInputRestrict <T>{
    T[] arr;
    int front = -1;
    int rear = -1;

    DequeImplementationInputRestrict(int sizeOfArr){
        arr = (T[]) new Object[sizeOfArr];
    }

    void enqueueRear(T item){
        if(front == -1 && rear == -1){
            front = 0;
            rear = 0;
            arr[rear] = item;
        } else if(rear == arr.length - 1){
            System.out.println("Overflow Error: Deque is full.");
        } else {
            rear++;
            arr[rear] = item;
        }
    }

    T dequeueRear(){
        if(front == -1 && rear == -1){
            System.out.println("Underflow Error: Deque is empty.");
            return null;
        } else if(front == rear){
            T item = arr[rear];
            front = -1;
            rear = -1;
            return item;
        } else {
            T item = arr[rear];
            rear--;
            return item;
        }
    }

    T dequeueFront(){
        if(front == -1 && rear == -1){
            System.out.println("Underflow Error: Deque is empty.");
            return null;
        } else if(front == rear){
            T item = arr[front];
            front = -1;
            rear = -1;
            return item;
        } else {
            T item = arr[front];
            front++;
            return item;
        }
    }

    void displayDeque(){
        if(front == -1 && rear == -1){
            System.out.println("[]");
            return;
        }
        System.out.print("[");
        for(int i = front; i <= rear; i++){
            System.out.print(arr[i]);
            if(i != rear) System.out.print(",");
        }
        System.out.println("]");
    }

}













package deque;
public class DequeImplementationOutputRestrict<T> {

    T[] arr;
    int front = -1;
    int rear  = -1;

    DequeImplementationOutputRestrict(int size) {
        arr = (T[]) new Object[size];
    }

    boolean isEmpty() {
        return front == -1 && rear == -1;
    }

    boolean isFull() {
        return rear == arr.length - 1 && front == 0;
    }

    void enqueueRear(T item) {
        if (isEmpty()) {
            front = 0;
            rear  = 0;
            arr[rear] = item;
        } else if (rear == arr.length - 1) {
            System.out.println("Overflow Error: no space at rear.");
        } else {
            rear++;
            arr[rear] = item;
        }
    }

    void enqueueFront(T item) {
        if (isEmpty()) {
            front = 0;
            rear  = 0;
            arr[front] = item;
        } else if (front == 0) {
            System.out.println("Overflow Error: no space at front.");
        } else {
            front--;
            arr[front] = item;
        }
    }

    T dequeueFront() {
        if (isEmpty()) {
            System.out.println("Underflow Error: Deque is empty.");
            return null;
        } else if (front == rear) {
            T item = arr[front];
            front = -1;
            rear  = -1;
            return item;
        } else {
            T item = arr[front];
            front++;
            return item;
        }
    }

    void displayDeque() {
        if (isEmpty()) {
            System.out.println("[]");
            return;
        }
        System.out.print("[");
        for (int i = front; i <= rear; i++) {
            System.out.print(arr[i]);
            if (i != rear) System.out.print(", ");
        }
        System.out.println("]");
    }
}





















package deque;

import java.util.Scanner;

public class MainDequeLabTask {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        int typeChoice;

        do {
            System.out.println("   Double Ended Queue (DEQueue) Menu   ");
            System.out.println("1. Input-Restricted  Deque");
            System.out.println("2. Output-Restricted Deque");
            System.out.println("0. Exit");
            System.out.print("Choose deque type: ");
            typeChoice = sc.nextInt();

            switch (typeChoice) {
                case 1:
                    runInputRestricted();
                    break;
                case 2:
                    runOutputRestricted();
                    break;
                case 0:
                    System.out.println("Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }

        } while (typeChoice != 0);

        sc.close();
    }

    static void runInputRestricted() {

        System.out.print("\nEnter size of deque: ");
        int size = sc.nextInt();

        CircularDequeInputRestrict<Integer> deque = new CircularDequeInputRestrict<>(size);

        int choice;

        do {
            System.out.println("\n--- Input-Restricted Deque ---");
            System.out.println("  (Insert: rear only | Delete: both ends)");
            System.out.println("1. Insert at Rear");
            System.out.println("2. Delete from Front");
            System.out.println("3. Delete from Rear");
            System.out.println("4. Display");
            System.out.println("0. Back to main menu");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value: ");
                    deque.enqueueRear(sc.nextInt());
                    break;
                case 2:
                    Integer rf = deque.dequeueFront();
                    if (rf != null) System.out.println("Deleted from front: " + rf);
                    break;
                case 3:
                    Integer rr = deque.dequeueRear();
                    if (rr != null) System.out.println("Deleted from rear: " + rr);
                    break;
                case 4:
                    System.out.print("Deque: ");
                    deque.display();
                    break;
                case 0:
                    System.out.println("Returning to main menu...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }

        } while (choice != 0);
    }

    static void runOutputRestricted() {

        System.out.print("\nEnter size of deque: ");
        int size = sc.nextInt();

        CircularDequeOutputRestrict<Integer> deque = new CircularDequeOutputRestrict<>(size);

        int choice;

        do {
            System.out.println("\n--- Output-Restricted Deque ---");
            System.out.println("  (Insert: both ends | Delete: front only)");
            System.out.println("1. Insert at Front");
            System.out.println("2. Insert at Rear");
            System.out.println("3. Delete from Front");
            System.out.println("4. Display");
            System.out.println("0. Back to main menu");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter value: ");
                    deque.enqueueFront(sc.nextInt());
                    break;
                case 2:
                    System.out.print("Enter value: ");
                    deque.enqueueRear(sc.nextInt());
                    break;
                case 3:
                    Integer removed = deque.dequeueFront();
                    if (removed != null) System.out.println("Deleted from front: " + removed);
                    break;
                case 4:
                    System.out.print("Deque: ");
                    deque.display();
                    break;
                case 0:
                    System.out.println("Returning to main menu...");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }

        } while (choice != 0);
    }
}
















package deque;
import java.util.Scanner;

public class MainForDeque {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of Deque: ");
        int size = sc.nextInt();

        DequeImplementationInputRestrict<Integer> deque = new DequeImplementationInputRestrict<>(size);

        int choice;

        do {
            System.out.println("\n===== DEQUE MENU (Input-Restricted) =====");
            System.out.println("1. Enqueue Rear  (insert at rear only)");
            System.out.println("2. Dequeue Front (remove from front)");
            System.out.println("3. Dequeue Rear  (remove from rear)");
            System.out.println("4. Display");
            System.out.println("0. Exit");
            System.out.print("Enter your choice: ");

            choice = sc.nextInt();

            switch (choice) {

                case 1:
                    System.out.print("Enter value to insert at rear: ");
                    int val = sc.nextInt();
                    deque.enqueueRear(val);
                    break;

                case 2:
                    Integer removedFront = deque.dequeueFront();
                    if (removedFront != null) {
                        System.out.println("Removed from front: " + removedFront);
                    }
                    break;

                case 3:
                    Integer removedRear = deque.dequeueRear();
                    if (removedRear != null) {
                        System.out.println("Removed from rear: " + removedRear);
                    }
                    break;

                case 4:
                    System.out.print("Deque: ");
                    deque.displayDeque();
                    break;

                case 0:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid choice. Try again.");
            }

        } while (choice != 0);

        sc.close();
    }
}

















