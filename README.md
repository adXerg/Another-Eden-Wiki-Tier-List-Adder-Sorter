# Another Eden Wiki's Altema Tier List Adder/Sorter
A simple python script to add/sort [Another Eden Wiki's Altema Tier List](https://anothereden.miraheze.org/wiki/Tier_Lists/Altema) .
This simple program will add and sort (by Grade first, then by Name alphabetically) automatically the script for the 'Edit' page.

Instructions:
1. In the 'New lines to add:' text box, input lines to be added separated by new line (Leave empty if you only want to sort).
Example:
  ```
  {{Tier list row|Yuna (Another Style)|AS|97|https://altema.jp/anaden/chara/752|role=Healer}}
  {{Tier list row|Shanie (Another Style)|AS|94|https://altema.jp/anaden/chara/750}}
  {{Tier list row|Gariyu (Another Style)|AS|93|https://altema.jp/anaden/chara/754}}
  ```
2. In the 'Old page script:' text box, copy **ALL** of the latest page script (You can get this from the 'Edit' page).
Example:
  ```
  <noinclude>{{Notice Tier List}}</noinclude>
  {| class="anotherTable sortable chara-table" style="display:inline-block; background:rgba(255,255,255,.4); margin:auto; overflow-y:scroll; height:800px"
  |+<div style="font-size:1.2em;">[https://altema.jp/anaden/charalist-2 Altema Character Evaluation List]</div>
  ! Icon || Character || Equip Types || Element || Rarity || Grade || Altema Character Page Link
  {{Tier list row|Felmina|5|97|https://altema.jp/anaden/chara/191}}
  {{Tier list row|Yuna (Another Style)|AS|97|https://altema.jp/anaden/chara/752|role=Healer}}
  {{Tier list row|Nagi (Another Style)|AS|96|https://altema.jp/anaden/chara/486}}
  {{Tier list row|Dunarith|5|95|https://altema.jp/anaden/chara/748|role=Healer}}
  {{Tier list row|Suzette|5|95|https://altema.jp/anaden/chara/2}}
  ...
  {{Tier list row|Jade|4|57|https://altema.jp/anaden/chara/141#1}}
  {{Tier list row|Yazuki|4|57|https://altema.jp/anaden/chara/176#1}}
  {{Tier list row|Benedict|4|56|https://altema.jp/anaden/chara/43#1}}
  {{Tier list row|Myron|4|56|https://altema.jp/anaden/chara/33#1}}
  {{Tier list row|Joker|4|--|https://altema.jp/anaden/chara/781}}
  |}
  ```
3. Click on 'Submit' button
4. Copy-Paste the new page script to the 'Edit' page

Screenshot:
![alt text](https://raw.githubusercontent.com/adXerg/Another-Eden-Wiki-Tier-List-Adder-Sorter/master/ss.PNG)

## **Download [here](https://github.com/adXerg/Another-Eden-Wiki-Tier-List-Adder-Sorter/releases/latest)**.
