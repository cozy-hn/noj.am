package java;
import java.util.*;

public class 핸드폰_요금{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] call = new int[N];
        for (int i = 0; i < N; i++)
            call[i] = in.nextInt();
        int Y = 0;
        int M = 0;
        for (int i = 0; i < N; i++){
            Y += (call[i] / 30 + 1) * 10;
            M += (call[i] / 60 + 1) * 15;
        }
        if (Y < M)
            System.out.println("Y " + Y);
        else if (Y > M)
            System.out.println("M " + M);
        else
            System.out.println("Y M " + Y);
    }
}