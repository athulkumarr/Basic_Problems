class Solution {
    public int minGroups(int[][] intervals) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        for(int[] interval : intervals) {
            if(!minHeap.isEmpty() && interval[0]>minHeap.peek())
                minHeap.poll();
            minHeap.offer(interval[1]);
        }
        return minHeap.size();
    }
    public static void main(String args[]) {
      int[][] intervals = {{5,10},{6,8},{1,5},{2,3},{1,10};
      System.out.println(minGroups(intervals));
    }
}
