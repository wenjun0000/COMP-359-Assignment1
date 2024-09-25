package app;

import java.util.*;

public class SpeedTest {
    public static void main(String[] args) {
        randomItemToSearch();

        manyRepeatedItemToSearch();


    }

    /**
     * search  many repeated items  in unique size array
     */
    private static void manyRepeatedItemToSearch() {
        System.out.println("Many Repeated Items to Search ...");
        Random random = new Random(System.currentTimeMillis());
        int size = 10_000; //how many items in list (list 1)
        int searchSize = 50_000; // how many items in list (list 2), we search for each element in list 2 on list 1.
        int degree = 10; // how many distinct items in list 2


        //generate unique data. the sequential search method will work on it.
        List<Integer> list = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            int data = i + 1;
            list.add(data);
        }
        //make the list random
        Collections.shuffle(list);
        list = new LinkedList<>(list);


        //prepare frequency sequential search list
        FrequencySequentialSearchList<Integer> myList = new FrequencySequentialSearchList<>();
        for (Integer integer : list) {
            myList.append(integer);
        }


        //prepare the data we searched for.
        LinkedList<Integer> data = new LinkedList<>();
        for (int i = 0; i < searchSize; i++) {
            data.addLast(random.nextInt(degree) + 1);
        }

        //test sequential search
        long arrayListTimeBegin = System.currentTimeMillis();
        for (Integer datum : data) {
            list.indexOf(datum);
        }
        long arrayListTimeEnd = System.currentTimeMillis();


        long listUsedTime = arrayListTimeEnd - arrayListTimeBegin;


        //test frequency sequential search
        long myListTimeBegin = System.currentTimeMillis();
        for (Integer datum : data) {
            myList.findIndex(datum);
        }
        long myListTimeEnd = System.currentTimeMillis();

        long myListUsedTime = myListTimeEnd - myListTimeBegin;


        System.out.printf("[Problem Size: %d, Search counting: %d] Frequency Sequential Search Time Used: %d ms\n", size, searchSize, myListUsedTime);
        System.out.printf("[Problem Size: %d, Search counting: %d] Sequential Search Time Used: %d ms\n", size, searchSize, listUsedTime);
    }

    /**
     * search random items.
     */
    private static void randomItemToSearch() {
        System.out.println("Random Items to Search ...");
        Random random = new Random(System.currentTimeMillis());
        int size = 10_000;
        int searchSize = 50_000;
        int degree = 10_000;

        List<Integer> list = new ArrayList<>(size);
        for (int i = 0; i < size; i++) {
            int data = i + 1;
            list.add(data);
        }
        Collections.shuffle(list);
        list = new LinkedList<>(list);

        FrequencySequentialSearchList<Integer> myList = new FrequencySequentialSearchList<>();
        for (Integer integer : list) {
            myList.append(integer);
        }

        LinkedList<Integer> data = new LinkedList<>();
        for (int i = 0; i < searchSize; i++) {
            data.addLast(random.nextInt(degree));
        }

        long arrayListTimeBegin = System.currentTimeMillis();
        for (Integer datum : data) {
            list.indexOf(datum);
        }
        long arrayListTimeEnd = System.currentTimeMillis();


        long listUsedTime = arrayListTimeEnd - arrayListTimeBegin;


        long myListTimeBegin = System.currentTimeMillis();
        for (Integer datum : data) {
            myList.findIndex(datum);
        }
        long myListTimeEnd = System.currentTimeMillis();

        long myListUsedTime = myListTimeEnd - myListTimeBegin;


        System.out.printf("[Problem Size: %d, Search counting: %d] Frequency Sequential Search Time Used: %d ms\n", size, searchSize, myListUsedTime);
        System.out.printf("[Problem Size: %d, Search counting: %d] Sequential Search Time Used: %d ms\n", size, searchSize, listUsedTime);
    }
}
