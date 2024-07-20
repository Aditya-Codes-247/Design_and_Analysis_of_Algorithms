class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int n_rows = matrix.size();
        int n_cols = n_rows > 0 ? matrix[0].size(): 0;
        int sel_idx = 0;
        for (int i = 0; i < n_rows; i++){
            if((target <= matrix[i][n_cols - 1]) && (target >= matrix[i][0])){
                sel_idx = i;
                std::cout << sel_idx;
            }
            else{
                continue;
            }
        }
        for (int i = 0; i< n_cols; i++){
            std::cout << i;
            if(target == matrix[sel_idx][i]){
                return true;
            }
            else{
                continue;
            }
        }
        return false;
    }
};