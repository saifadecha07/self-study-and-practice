//okay ba babe test
void main() {
  // output to display
  print("Hi man");
  print("เฟี้ยวนะ");
  int a = 1, b = 2, c;
  num k = 10.1;
  var mon = 100;
  mon = 10;
  const j = 10;
  print("a+b=${a + b}");
  int m = (a == 10) ? 5 : 6;
  print(m);
  dynamic month = "f";
  var goal = "";
  switch (month) {
    case "jan":
      goal = "1";
      break;
    case "feb":
      goal = "2";
    default:
      print("NO");
  }
  print(goal);
  mon = 20;
  print(mon);
  show(0);
  List l1 = []; //can be different type
  List<String> l2 = []; //same type
  var l3 = [];
  l3.add(2);
  for (int i = 1; i <= 100; i++) {
    l1.add(i);
  }
  for (var item in l1) {
    print(item);
  }
}

void show(int a) {
  do {
    print("hello");
    a++;
  } while (a < 3);
}

getN() => print("ss");
int getM() => 5;
