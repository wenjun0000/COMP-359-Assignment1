package app;

import java.util.*;

/**
 * Implement a program that orders keys based on user query frequency during execution.
 * That is, update the order over the use of the program so that sequential search operates faster.
 *
 * @param <T> data type
 */
public class FrequencySequentialSearchList<T> {
    private int size;
    private final Node<T> head = new Node<>();
    private final Node<T> tail = new Node<>();

    /**
     * find data in the sequence.
     * and update keys order.
     *
     * @param data data to find
     * @return the position and freq before find.
     */
    public IndexWithFreq findIndex(T data) {
        Node<T> node = head.getNext();
        int index = 0;
        while (node != tail) {
            if (Objects.equals(node.getData(), data)) {
                IndexWithFreq result = new IndexWithFreq(index, node.getFreq());
                justifyByFrequency(node);
                return result;
            }


            index++;
            node = node.getNext();
        }
        return null;
    }

    /**
     * adjust frequency
     *
     * @param node the node in the doubly linked list
     */
    private void justifyByFrequency(Node<T> node) {
        node.setFreq(node.getFreq() + 1);

        //max one
        Node<T> left = node.getPre();

        while (left != head && left.getFreq() <= node.getFreq()) {
            left = left.getPre();
        }

        /*
         *              A  H           J  C  E
         *  -------------  -------------  -  ------------------
         *
         * A's freq > C or A is head
         *
         */

        var A = left;
        var H = left.getNext();
        var J = node.getPre();
        var C = node;
        var E = node.getNext();

        if (H != C) {
            A.setNext(C);
            C.setPre(A);
            C.setNext(H);
            H.setPre(C);
            J.setNext(E);
            E.setPre(J);
        }


    }


    /**
     * constructor
     */
    public FrequencySequentialSearchList() {
        size = 0;
        head.setNext(tail);
        tail.setPre(head);
    }

    /**
     * size in the list
     *
     * @return list size
     */
    public int size() {
        return size;
    }

    /**
     * check if list is empty
     *
     * @return true if empty, false otherwise.
     */
    public boolean isEmpty() {
        return size == 0;
    }



    /**
     * add data to last of list
     *
     * @param data data to add
     */
    public void append(T data) {
        Node<T> left = tail.getPre();
        Node<T> right = tail;
        Node<T> node = new Node<>(0, left, right, data);
        left.setNext(node);
        right.setPre(node);
        size++;
    }




    /**
     * remote item at index
     *
     * @param index the index item has
     * @return removed item
     */
    public T remove(int index) {

        Node<T> targetNode = head.getNext();

        {
            int i = 0;
            while (i < index) {
                i++;
                targetNode = targetNode.getNext();
            }
        }


        T data = targetNode.getData();

        Node<T> left = targetNode.getPre();

        Node<T> right = targetNode.getNext();

        left.setNext(right);
        right.setPre(left);
        size--;

        return data;
    }

    /**
     * remove first occurred element
     *
     * @param element the element to remove
     * @return removed data
     */

    public T remove(T element) {

        Node<T> targetNode = head.getNext();
        boolean found = false;
        {
            while (targetNode != tail) {
                if (Objects.equals(targetNode.getData(), element)) {
                    found = true;
                    break;
                }
                targetNode = targetNode.getNext();
            }
        }

        if (!found) {
            return null;
        }

        T data = targetNode.getData();

        Node<T> left = targetNode.getPre();

        Node<T> right = targetNode.getNext();

        left.setNext(right);
        right.setPre(left);
        size--;

        return data;
    }

    /**
     * get data at some index and update frequency
     *
     * @param index the index
     * @return data
     */
    public T get(int index) {
        Node<T> targetNode = head.getNext();

        {
            int i = 0;
            while (i < index) {
                i++;
                targetNode = targetNode.getNext();
            }
        }
        T data = targetNode.getData();

        justifyByFrequency(targetNode);

        return data;
    }


    public record IndexWithFreq(int index, int freq) {
    }

    ;

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof FrequencySequentialSearchList<?>) {
            FrequencySequentialSearchList<?> list2 = (FrequencySequentialSearchList<?>) obj;
            if (size() != list2.size()) {
                return false;
            } else {
                Node<T> node1 = head.getNext();
                Node<?> node2 = list2.head.getNext();
                while (node1 != tail) {
                    T data1 = node1.getData();
                    Object data2 = node2.getData();

                    if (!Objects.equals(data1, data2)) {
                        return false;
                    }


                    node1 = node1.getNext();
                    node2 = node2.getNext();
                }
                return true;
            }
        }
        return false;
    }


    @Override
    public int hashCode() {

        int result = 1;
        result = 31 * result + Objects.hashCode(this.size);

        Node<T> node1 = head.getNext();
        while (node1 != tail) {
            T data1 = node1.getData();

            result = 31 * result + Objects.hashCode(data1);

            node1 = node1.getNext();
        }
        return result;
    }
}

/**
 * represent a node with frequency and data
 *
 * @param <T>
 */
class Node<T> {
    private int freq;
    private Node<T> pre;
    private Node<T> next;
    private T data;

    public Node(int freq, Node<T> pre, Node<T> next, T data) {
        this.freq = freq;
        this.pre = pre;
        this.next = next;
        this.data = data;
    }

    public int getFreq() {
        return freq;
    }

    public void setFreq(int freq) {
        this.freq = freq;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public Node<T> getPre() {
        return pre;
    }

    public void setPre(Node<T> pre) {
        this.pre = pre;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public Node() {
    }
}