// 金数据表单自动填写 - 单体
// Author: wzx1210
// Date: 2022-12-29
// Version: 1.0
// Path: autoForm.js
// Utilise: 浏览器脚本

// 模拟react点击事件
const mouseClickEvents = ['mousedown', 'click', 'mouseup'];
function simulateMouseClick(element){
  mouseClickEvents.forEach(mouseEventType =>
    element.dispatchEvent(
      new MouseEvent(mouseEventType, {
          view: window,
          bubbles: true,
          cancelable: true,
          buttons: 1
      })
    )
  );
}

//模拟react输入
function simulateInput(element,value) {
 let input = element;
 let lastValue = input.value;
 input.value = value;

 let event = new Event('input', { bubbles: true });
 event.simulated = true;

 let tracker = input._valueTracker;

 if (tracker) {
       tracker.setValue(lastValue);
 }
 input.dispatchEvent(event);
}

//填写文本信息
var inputElement=document.querySelectorAll('div.ant-form-item-control-input > div > span > span > input');
simulateInput(inputElement[0],'*your name*');
simulateInput(inputElement[1],'*your student id*');
simulateInput(inputElement[2],'*your class*');

//填写选择信息
var selectElement=document.getElementsByClassName('pretty-select__control');
simulateMouseClick(selectElement[0]);
var selected=document.querySelector('#react-select-2-option-6');
console.log(selected)
selected.click();

//提交
var btn=document.querySelector('button');
btn.click();
