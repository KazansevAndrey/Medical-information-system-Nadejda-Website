const analyzesContainer = $('#dropdown_analyzes');
const examinationsContainer = $('#dropdown_examinations');
const diagnosesContainer = $('#dropdown_diagnoses');
const diariesContainer = $('#dropdown_diaries');
const itemsContainer = $('#items-container');



// Категории 
function showCategoriesBlock() {
    document.getElementById('categories-block').style.display = 'block';
    document.getElementById('no-category-block').style.display = 'none';
}
// Чисто записи без категорий
function showNoCategoryBlock() {
    document.getElementById('categories-block').style.display = 'none';
    document.getElementById('no-category-block').style.display = 'block';
}
function update_categories(data){
    analyzesContainer.empty();
    examinationsContainer.empty();
    diagnosesContainer.empty();
    diariesContainer.empty();

    document.getElementById('analyzes-count').textContent = `(${data.analyzes_count || 0})`;
    document.getElementById('examinations-count').textContent = `(${data.examinations_count || 0})`;
    document.getElementById('diagnoses-count').textContent = `(${data.diagnoses_count || 0})`;
    document.getElementById('diaries-count').textContent = `(${data.diaries_count || 0})`;
}

function getTemplate(item){
    if(item.type=='analysis'){
        return analisisItemTemplate;
    }
    else if(item.type=='diagnose'){
        return diagnoseItemTemplate;
    }
    else if(item.type=='diary'){
        return diaryItemTemplate;
    }
    else if(item.type=='examination'){
        return examinationItemTemplate;
    }
}

function FilterRecords(patient_id){
    var category = document.getElementById('categories').value;
    console.log(category)
    var date = document.getElementById('date').value;
    console.log(date)
    var list_type = document.getElementById('list_type').value;
    console.log(list_type)
    $.ajax({
        url: `/patient/${patient_id}/sorting`, 
        data: {
            'category': category,
            'date':date,
            'list_type':list_type
        },
        dataType: 'json',
        success: function(data) {
            if(category == 'all'){
                $('#list_type').prop('disabled', false);
                
                if(list_type == 'by_category'){
                    showCategoriesBlock()
                    update_categories(data) // Все очищаем и записываем count
                    data.analyzes.forEach(function(analysis){
                        analyzesContainer.append(analisisItemTemplate(analysis))})
                    
                    data.examinations.forEach(function(examination){
                        console.log(examination.date)
                        examinationsContainer.append(examinationItemTemplate(examination))})
                    
                    data.diagnoses.forEach(function(diagnose){
                        diagnosesContainer.append(diagnoseItemTemplate(diagnose))})

                    data.diaries.forEach(function(diarie){
                        diariesContainer.append(diaryItemTemplate(diarie))})
                    }

                else if (list_type == 'chronologically'){
                    
                    showNoCategoryBlock();
                    itemsContainer.empty();
                    data.items.forEach(function(item) {
                        template = getTemplate(item)
                        itemsContainer.append(template(item));
                })}}

            else{
                listTypeSelect = $('#list_type')
                listTypeSelect.val('chronologically')
                $('#list_type').prop('disabled', "by_category");
                
                showNoCategoryBlock();
                itemsContainer.empty();
                data.category_items.forEach(function(item) {
                    template = getTemplate(item)
                    itemsContainer.append(template(item));
            })
            
        }}})}
        

function search_analyses(patient_id){
    var query = document.getElementById('search-input').value;
    console.log("Активирована функция поиск анализов")
    $.ajax({
        url: `${patient_id}/search_analyses`, // URL для поиска пациентов
        data: {
            'q': query
        },
        dataType: 'json',
        success: function(data){
            itemsContainer.empty();
            showNoCategoryBlock();
            data.analyzes.forEach(function(analisis) {
                itemsContainer.append(analisisItemTemplate(analisis));
            })}
        }
    )
}
const analisisItemTemplate = (analysis) => `
<div class="dropdown-item" onclick="analyzes('${analysis.id}')">
              <div class="span-column">
                <span class="item-title">'${analysis.analysis_name}'</span>
                <span class="item-date">'${analysis.date}'</span>
              </div>
              <i class="fa-solid fa-arrow-right awesome"></i>
            </div>
`;

const examinationItemTemplate = (examination) => `
<div class="dropdown-item" onclick="inspections('${examination.id}')" id="d4">
              <div class="span-column">
                <span class="item-title">Первичный осмотр</span>
                <span class="item-date">${examination.date}</span>
              </div>
              <i class="fa-solid fa-arrow-right awesome"></i>
            </div>`

const diagnoseItemTemplate = (diagnose) => 
    `<div class="dropdown-item" onclick="diagnoses('${diagnose.id}')" id="d7">
              <div class="span-column">
                <span class="item-title">${diagnose.code}</span>
                <span class="item-date">${diagnose.date}</span>
                <span class="item-date">${diagnose.kind}</span>
              </div>
              <i class="fa-solid fa-arrow-right awesome"></i>
            </div>`

const diaryItemTemplate = (diary) =>
    `<div class="dropdown-item" onclick="diaries('${diary.id}')" id="d10">
              <div class="span-column">
                <span class="item-title">${diary.date}</span>
                <span class="item-date">${diary.additional}</span>
              </div>
              <i class="fa-solid fa-arrow-right awesome"></i>
            </div>`


