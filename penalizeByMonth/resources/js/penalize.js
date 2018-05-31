$(document).click(function(){
    $('.div-date').hide();
});
$('input').on('click', function(event){
    event.stopPropagation();
});
$('.date-year').on('click', function(event){
    event.stopPropagation();
});
$('input').click(alertDate);

//日期选择弹框
function alertDate(element){
    var width = this.clientWidth;
    var height = this.clientHeight;
    var top = this.offsetTop + height;
    var left = this.offsetLeft;
    $('.div-date').css('width', width);
    $('.div-date').css('top', top);
    $('.div-date').css('left', left);
    $('.div-date').css('display') == 'none' ? $('.div-date').show() : $('.div-date').hide();
}

//选择日期
$('#minus').click(function(){
    var year = $('#year').text();
    $('#year').text(--year);
});
$('#add').click(function(){
    var year = $('#year').text();
    $('#year').text(++year);
});
$('.date-month span').click(function(){
    var month = $(this).text();
    var year = $('#year').text();
    month = month < 10 ? '0' + month : month;
    var date = year + '-' + month;
    var start = document.getElementById('start').offsetLeft;
    var place_left = this.parentNode.parentNode.offsetLeft;
    var this_input = Math.abs(start - place_left) < 10 ? 'start' : 'end';
    var start_date = $('#start').val();
    var end_date = $('#end').val();
    var verify_result = verifyDate(this_input, date);
    verify_result[0] ? writeDate(start, place_left, date) : layer.alert(verify_result[1]);
});

//校验日期是否合法
function verifyDate(this_input, date){
    var start_date = $('#start').val();
    var end_date = $('#end').val();
    if(!start_date && !end_date)
        return [true, ''];
    var dates = {};
    dates['start'] = start_date;
    dates['end'] = end_date;
    date && (dates[this_input] = date);
    start_date = dates['start'].split('-');
    end_date = dates['end'].split('-');
    if(end_date[0] - start_date > 0)
        return [true, ''];
    if(end_date[0] != '' && end_date[0] - start_date[0] < 0)
        return [false, '结束年份不能小于开始年份'];
    if(end_date[1] - start_date[1] < 0)
        return [false, '结束月份不能小于开始月份'];
    return [true, ''];
}

//向输入框写入日期
function writeDate(start, left, date){
    Math.abs(start - left) < 10 ? $('#start').val(date) : $('#end').val(date);
    $('.div-date').hide();
}