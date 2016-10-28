clc;
%average the voxels before regressing
subjs = {'A','B','C','D','E','F','G','H','I'};
for i = 1:2
    fprintf('%i\n',i);
    subj = subjs{i};
    sc = load(sprintf('AndersonetalJOCN2014_TACL2016_FMRIDAT.mat'));
    word = sc.Participant(i).wordC;
    C = unique(word);
    A_percept = zeros(70,1);
    for j = 1:70
        len = length(C{j});
        A_percept(j)= len;
    end;
   
    % Average the voxels for each word before regressing.
    data_from_file = sc.Participant(i).datM2;
    data1 = [];
    for k=1:5:size(data_from_file,1)
        data1 = [data1;mean(data_from_file(k:k+4,:))];
    end
    % DO mean normalisation for the data
    data = zscore(data1);
    % load the features to be regressed out
    %percept = load(sprintf('Anderson_A_percept.mat'));
    % do Mean normalisation for regressed values
    p = zscore(A_percept);
    [weightMatrix, r] = learn_text_from_fmri_kernel_sep_lambda_no_bias( p,data, 1);
    fprintf('%.g\n',median(r))
    p_1 = p;
    p_1(:,end+1)=1;
    x_fit = p_1*weightMatrix;
    data = data - x_fit;
    data = reshape(data,size(data1));
    data(1:10,1:10)
    %save(sprintf('/Users/Dhanush/desktop/Regress_output/Anderson_raw_avrg_percept_residual_%s.mat',subj),'data','C','-v7.3');
end;

 