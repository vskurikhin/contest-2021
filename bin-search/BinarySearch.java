
public class BinarySearch {

    public BinarySearch(int[] arr, int x, int left, int right) {
        index = binarySearch(arr, x, 0, arr.length);
    }

    public getIndex() int {
        return index;
    }

    public static int binarySearch(int[] arr, int x, int left, int right) {
        if (right <= left) { // промежуток пуст
            return -1;
        }
        // промежуток не пуст
        int mid = (left + right) / 2;
        if (arr[mid] == x) {  // центральный элемент — искомый
            return mid;
        } else if (x < arr[mid]) { // искомый элемент меньше центрального значит следует искать в левой половине
            return binarySearch(arr, x, left, mid);
        } else { // иначе следует искать в правой половине
            return binarySearch(arr, x, mid + 1, right);
        }
    }

    // изначально мы запускаем двоичный поиск на всей длине массива
    int index = binarySearch(arr, x, 0, arr.length);
}