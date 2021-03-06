dir  = '/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Michell_Data/';
dir2 = '/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Michell_Data/MRI_VoxelDone/';
dir1 ='/Users/Dhanush/Desktop/Projects/Brain_Bench/GIT_DATA/Michell_Data/MRI_RegressDone/';
subjs1 = {'P1','P2','P3','P4','P5','P6','P7','P8','P9'};
for i = 1:9
    fprintf('%i\n',i);
    subj = subjs1{i};
    st = load(sprintf('%s%s_raw_notavrg_percept_residual_test.mat',dir1,subj));
    data1 = st.data;
    words = st.words;
    labels =st.labels;
    rep1 = 6;
    [words1, voxels1] = size(data1);
    c=1;
    data = zeros(size(data1));
    %Arrange the words as per the labels
    for j = 1:60
        for k=1:360
            if j==labels(k)
                data(c,:) = data1(k,:);
                c = c+1;
            end;
        end;
    end;
    %data1([29,113,146,181,288,353,21],1:10);
    %data(1:7,1:10)
    size(data)
    data = data';
   
    % Permute for Voxel * word * repetition format
   A1 = [];
   A1 = zeros(voxels1,60,6);
   for n = 1 :voxels1
       m = 1;
       for o = 1:60
         A1(n,o,:) = data(n,m:m+5);  
         m = m+6;
       end;
   end;
    size(A1)
    voxel_sel_A1 = voxel_selection(A1);
    %size(voxel_sel_A1)
    %voxel_sel_A1 = zscore(voxel_sel_A1);
   %voxel_sel_A1(1:5)
% Sorting the voxel scores in descending order
    [Asorted,AbsoluteIndices_A] = sort(voxel_sel_A1(:),'descend');
    Asorted(1:5)
% Selecting top 10% voxel
    toprated_A = voxels1 * 0.03;
    A_Indices_selected = AbsoluteIndices_A(1:toprated_A,1);
    %Asorted(1:5)
    
% Removing low scored voxels from data
    voxel_selected_A = [];
%voxel_selected_B = [];

    for index = 1:size(A_Indices_selected,1)
        voxel_selected_A =cat(2,voxel_selected_A,data1(:,A_Indices_selected(index,1)));
    end;

    size(voxel_selected_A)
 
    A_avg = [];
    for j = 1:60
        A_avg(j,:) = squeeze(mean(voxel_selected_A(labels == j,:)));
    end;

    size(A_avg)
    data = A_avg;
    save(sprintf('%s%s_voxselected.mat',dir2,subj),'data','labels','words','-v7.3');
end;





