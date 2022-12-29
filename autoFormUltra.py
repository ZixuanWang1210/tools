# 金数据表单自动填写 - Ultra
# Author: wzx1210
# Date: 2022-12-29
# Version: 1.0
# Path: autoFormUltra.py
# Input format: [class, name, id] without header

from selenium import webdriver
import time
import xlrd

script = """
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
var inputElement=document.querySelectorAll('div.ant-form-item-control-input > div > span > span > input');
simulateInput(inputElement[0],'%s');
simulateInput(inputElement[1],'%s');
simulateInput(inputElement[2],'%s');
var selectElement=document.getElementsByClassName('pretty-select__control');
simulateMouseClick(selectElement[0]);
var selected=document.querySelector('#react-select-2-option-6');
console.log(selected)
selected.click();
var btn=document.querySelector('button');
btn.click();
"""

if __name__ == "__main__":
    rd = xlrd.open_workbook('./input.xls').sheet_by_index(0)
    url = input("输入URL: ")
    driver = webdriver.Chrome()
    for rown in range(rd.nrows):
        driver.get(url)
        sClass = rd.cell_value(rown, 0)
        sName = rd.cell_value(rown, 1)
        sId = rd.cell_value(rown, 2)
        time.sleep(2)
        print("正在填写：",sName)
        driver.execute_script(script%(sName,sId,sClass))
        time.sleep(2)
    driver.quit()
