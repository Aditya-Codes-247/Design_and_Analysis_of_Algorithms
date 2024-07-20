int maxArea(int* height, int heightSize) {
    int maxArea=0;
    int left=0;
    int right=heightSize-1;
    while(left<right)
    {
        int currentArea;
        if(height[left]<height[right])
            currentArea=(right-left)*height[left];
        else
            currentArea=(right-left)*height[right];
        if (currentArea>maxArea)
            maxArea=currentArea;
        if (height[left]<height[right])
            left++;
        else
            right--;
    }
    return maxArea;   
}