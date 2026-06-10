import os
import random
import glob

snippets = {
    "python_basics": [
        "# Source: W3Schools Python Tutorial\n# Python Variables and Data Types\nx = 5\ny = 'John'\nprint(type(x))\nprint(type(y))\n\n# Casting\nx = str(3)    # x will be '3'\ny = int(3)    # y will be 3\nz = float(3)  # z will be 3.0",
        "# Source: W3Schools Python Tutorial\n# Python Lists\nthislist = ['apple', 'banana', 'cherry']\nprint(thislist[1])\n\n# Change Item Value\nthislist[1] = 'blackcurrant'\nprint(thislist)",
        "# Source: W3Schools Python Tutorial\n# Python Dictionaries\nthisdict = {\n  'brand': 'Ford',\n  'model': 'Mustang',\n  'year': 1964\n}\nprint(thisdict['brand'])\nthisdict['year'] = 2018",
        "# Source: Python Official Docs\n# Python If ... Else\na = 200\nb = 33\nif b > a:\n  print('b is greater than a')\nelif a == b:\n  print('a and b are equal')\nelse:\n  print('a is greater than b')",
        "# Source: W3Schools Python Tutorial\n# Python For Loops\nfruits = ['apple', 'banana', 'cherry']\nfor x in fruits:\n  print(x)\n  if x == 'banana':\n    break"
    ],
    "fastapi_practice": [
        "from fastapi import FastAPI\n\n# Source: FastAPI Official Docs\napp = FastAPI()\n\n# Path Parameters\n@app.get('/items/{item_id}')\ndef read_item(item_id: int, q: str = None):\n    return {'item_id': item_id, 'q': q}",
        "from fastapi import FastAPI\nfrom pydantic import BaseModel\n\n# Source: FastAPI Official Docs - Request Body\nclass Item(BaseModel):\n    name: str\n    price: float\n    is_offer: bool = None\n\napp = FastAPI()\n\n@app.post('/items/')\ndef create_item(item: Item):\n    return item",
        "from fastapi import FastAPI, Query\n\n# Source: FastAPI Official Docs - Query Parameters\napp = FastAPI()\n\n@app.get('/items/')\nasync def read_items(q: str | None = Query(default=None, max_length=50)):\n    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}\n    if q:\n        results.update({'q': q})\n    return results"
    ],
    "postgres_db": [
        "-- Source: W3Schools SQL Tutorial\n-- PostgreSQL SELECT Statement\nSELECT * FROM customers;\n\n-- SELECT DISTINCT\nSELECT DISTINCT country FROM customers;",
        "-- Source: W3Schools SQL Tutorial\n-- PostgreSQL WHERE Clause\nSELECT * FROM customers WHERE country = 'Mexico';\n\n-- AND, OR, NOT\nSELECT * FROM customers WHERE country = 'Germany' AND city = 'Berlin';",
        "-- Source: W3Schools SQL Tutorial\n-- PostgreSQL ORDER BY\nSELECT * FROM customers ORDER BY country DESC;\n\n-- INSERT INTO\nINSERT INTO customers (customer_name, contact_name, country) VALUES ('Cardinal', 'Tom B. Erichsen', 'Norway');",
        "-- Source: PostgreSQL Official Docs\n-- PostgreSQL UPDATE\nUPDATE customers SET contact_name = 'Alfred Schmidt', city= 'Frankfurt' WHERE customer_id = 1;\n\n-- DELETE\nDELETE FROM customers WHERE customer_name='Alfreds Futterkiste';"
    ],
    "nestjs_basics": [
        "import { Controller, Get, Post, Body } from '@nestjs/common';\n\n// Source: NestJS Official Documentation - Controllers\n@Controller('cats')\nexport class CatsController {\n  @Post()\n  create(@Body() createCatDto: any) {\n    return 'This action adds a new cat';\n  }\n\n  @Get()\n  findAll(): string {\n    return 'This action returns all cats';\n  }\n}",
        "import { Injectable } from '@nestjs/common';\n\n// Source: NestJS Official Documentation - Providers\nexport interface Cat { name: string; age: number; breed: string; }\n\n@Injectable()\nexport class CatsService {\n  private readonly cats: Cat[] = [];\n\n  create(cat: Cat) {\n    this.cats.push(cat);\n  }\n\n  findAll(): Cat[] {\n    return this.cats;\n  }\n}",
        "import { Module } from '@nestjs/common';\nimport { CatsController } from './cats.controller';\nimport { CatsService } from './cats.service';\n\n// Source: NestJS Official Documentation - Modules\n@Module({\n  controllers: [CatsController],\n  providers: [CatsService],\n})\nexport class CatsModule {}"
    ],
    "data_science": [
        "import pandas as pd\n\n# Source: Kaggle Pandas Tutorial\n# Read CSV\ndf = pd.read_csv('data.csv')\n\n# Display basic info\nprint(df.head())\nprint(df.info())\nprint(df.describe())",
        "import pandas as pd\nimport numpy as np\n\n# Source: Towards Data Science - Data Cleaning\n# Handling missing values\ndf = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})\n\n# Fill missing values\ndf.fillna(value=0, inplace=True)\nprint(df)",
        "import matplotlib.pyplot as plt\nimport numpy as np\n\n# Source: W3Schools Matplotlib Tutorial\n# Basic plotting\nxpoints = np.array([1, 8])\nypoints = np.array([3, 10])\n\nplt.plot(xpoints, ypoints)\nplt.show()"
    ],
    "machine_learning": [
        "from sklearn.model_selection import train_test_split\nfrom sklearn.linear_model import LogisticRegression\nimport numpy as np\n\n# Source: Scikit-Learn Official Docs\nX = np.array([[1], [2], [3], [4], [5]])\ny = np.array([2, 4, 6, 8, 10])\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n\nmodel = LogisticRegression()\nmodel.fit(X_train, y_train)\nprint('Score:', model.score(X_test, y_test))",
        "from sklearn.tree import DecisionTreeClassifier\n\n# Source: Google Machine Learning Crash Course\n# Simple Decision Tree\nfeatures = [[140, 1], [130, 1], [150, 0], [170, 0]] # weight, texture (1=smooth, 0=bumpy)\nlabels = [0, 0, 1, 1] # 0=apple, 1=orange\n\nclf = DecisionTreeClassifier()\nclf = clf.fit(features, labels)\nprint('Prediction:', clf.predict([[160, 0]]))",
        "from sklearn.cluster import KMeans\nimport numpy as np\n\n# Source: Towards Data Science - K-Means Clustering\nX = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])\nkmeans = KMeans(n_clusters=2, random_state=0, n_init='auto').fit(X)\nprint('Labels:', kmeans.labels_)\nprint('Centers:', kmeans.cluster_centers_)"
    ],
    "data_structures": [
        "# Source: GeeksforGeeks - Data Structures\nclass Stack:\n    def __init__(self):\n        self.items = []\n\n    def push(self, item):\n        self.items.append(item)\n\n    def pop(self):\n        return self.items.pop() if not self.is_empty() else None\n\n    def is_empty(self):\n        return len(self.items) == 0",
        "# Source: GeeksforGeeks - Queue Data Structure\nclass Queue:\n    def __init__(self):\n        self.items = []\n\n    def enqueue(self, item):\n        self.items.insert(0, item)\n\n    def dequeue(self):\n        return self.items.pop() if not self.is_empty() else None\n\n    def is_empty(self):\n        return len(self.items) == 0",
        "# Source: LeetCode Practice Notes\nclass BinaryTreeNode:\n    def __init__(self, data):\n        self.data = data\n        self.left = None\n        self.right = None\n\n# Create root\nroot = BinaryTreeNode(10)\nroot.left = BinaryTreeNode(5)\nroot.right = BinaryTreeNode(15)"
    ],
    "algorithms": [
        "# Source: Grokking Algorithms Book\ndef binary_search(arr, low, high, x):\n    if high >= low:\n        mid = (high + low) // 2\n        if arr[mid] == x:\n            return mid\n        elif arr[mid] > x:\n            return binary_search(arr, low, mid - 1, x)\n        else:\n            return binary_search(arr, mid + 1, high, x)\n    else:\n        return -1",
        "# Source: GeeksforGeeks - Sorting Algorithms\ndef merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr)//2\n        L = arr[:mid]\n        R = arr[mid:]\n        merge_sort(L)\n        merge_sort(R)\n        i = j = k = 0\n        while i < len(L) and j < len(R):\n            if L[i] < R[j]:\n                arr[k] = L[i]\n                i += 1\n            else:\n                arr[k] = R[j]\n                j += 1\n            k += 1\n        while i < len(L):\n            arr[k] = L[i]\n            i += 1\n            k += 1\n        while j < len(R):\n            arr[k] = R[j]\n            j += 1\n            k += 1",
        "# Source: HackerRank Algorithms Practice\ndef quick_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quick_sort(left) + middle + quick_sort(right)"
    ],
    "docker_practice": [
        "# Source: Docker Official Documentation\nFROM node:18-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm install\nCOPY . .\nEXPOSE 3000\nCMD [\"npm\", \"start\"]",
        "# Source: FastAPI Docker Deployment Guide\nFROM python:3.9-slim\nWORKDIR /code\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nCMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"80\"]",
        "# Source: Docker Compose Getting Started\nversion: '3.8'\nservices:\n  web:\n    build: .\n    ports:\n      - '8000:8000'\n    depends_on:\n      - db\n  db:\n    image: postgres:13\n    environment:\n      POSTGRES_USER: postgres\n      POSTGRES_PASSWORD: password"
    ]
}

dates = ['Morning study session', 'Late night coding', 'Weekend practice', 'Reviewing docs before bed', 'Lunch break learning']
moods = ['Finally understood this concept!', 'Need to memorize this syntax.', 'W3Schools explanation is really clear.', 'This took a while to debug, but it works now.', 'Awesome feature.']

for dir_name, options in snippets.items():
    if not os.path.exists(dir_name):
        continue
    files = glob.glob(os.path.join(dir_name, '*.*'))
    for file_path in files:
        content = random.choice(options)
        comment_prefix = '--' if file_path.endswith('.sql') else ('//' if file_path.endswith('.ts') else '#')
        header = f"{comment_prefix} Session: {random.choice(dates)}\n{comment_prefix} Note: {random.choice(moods)}\n\n"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(header + content)

print(f"Enriched files across {len(snippets)} directories.")
