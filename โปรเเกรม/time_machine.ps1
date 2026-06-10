$ErrorActionPreference = 'Stop'
$startDate = [datetime]"2025-10-15"
$endDate = [datetime]"2026-04-06"

$topics = @(
    @{ ext="py"; dir="python_basics"; code="print('Hello Python Data Science')"; msg="Practice Python basic syntax" },
    @{ ext="py"; dir="fastapi_practice"; code="from fastapi import FastAPI`n`napp = FastAPI()`n`n@app.get('/')`ndef read_root():`n    return {'status': 'ok'}"; msg="Setup basic FastAPI server" },
    @{ ext="sql"; dir="postgres_db"; code="CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(50));"; msg="Create users table in PostgreSQL" },
    @{ ext="ts"; dir="nestjs_basics"; code="import { Controller, Get } from '@nestjs/common';`n`n@Controller()`nexport class AppController {`n  @Get()`n  getHello(): string {`n    return 'Hello NestJS!';`n  }`n}"; msg="Create NestJS AppController" },
    @{ ext="py"; dir="data_science"; code="import pandas as pd`n`ndf = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})`nprint(df.head())"; msg="Practice Pandas DataFrame operations" },
    @{ ext="py"; dir="machine_learning"; code="from sklearn.linear_model import LinearRegression`n`nmodel = LinearRegression()`nprint('Model initialized')"; msg="Initialize ML Linear Regression model" },
    @{ ext="py"; dir="data_structures"; code="class Node:`n    def __init__(self, data):`n        self.data = data`n        self.next = None"; msg="Implement LinkedList Node structure" },
    @{ ext="py"; dir="algorithms"; code="def bubble_sort(arr):`n    n = len(arr)`n    for i in range(n):`n        for j in range(0, n-i-1):`n            if arr[j] > arr[j+1]:`n                arr[j], arr[j+1] = arr[j+1], arr[j]"; msg="Implement Bubble Sort algorithm" },
    @{ ext="yaml"; dir="docker_practice"; code="version: '3.8'`nservices:`n  db:`n    image: postgres:13`n    environment:`n      POSTGRES_USER: user"; msg="Setup basic docker-compose for database" }
)

$currentDate = $startDate
$commitCount = 0
$lastMonth = 0

Write-Host "Starting Time Machine from $($startDate.ToString('yyyy-MM-dd')) to $($endDate.ToString('yyyy-MM-dd'))..."

while ($currentDate -le $endDate) {
    if ($currentDate.Month -ne $lastMonth) {
        Write-Host "Processing $($currentDate.ToString('MMMM yyyy'))..."
        $lastMonth = $currentDate.Month
    }

    # Generate 4 to 6 commits a day
    $numCommits = Get-Random -Minimum 4 -Maximum 7
    for ($i = 0; $i -lt $numCommits; $i++) {
        $topic = $topics | Get-Random
        
        $targetDir = $topic.dir
        if (-not (Test-Path $targetDir)) {
            New-Item -ItemType Directory -Path $targetDir | Out-Null
        }

        # Generate a realistic time during the day (e.g., 9 AM to 11 PM)
        $timeOffset = Get-Random -Minimum 9 -Maximum 23
        $minOffset = Get-Random -Minimum 0 -Maximum 59
        $secOffset = Get-Random -Minimum 0 -Maximum 59
        
        $commitTime = $currentDate.AddHours($timeOffset).AddMinutes($minOffset).AddSeconds($secOffset)
        $dateStr = $commitTime.ToString("yyyy-MM-ddTHH:mm:ss")
        
        $filename = "$targetDir\practice_$($commitTime.ToString('yyyyMMdd_HHmmss')).$($topic.ext)"
        
        # Write small code snippet
        Set-Content -Path $filename -Value $topic.code
        
        # Git operations
        git add $filename
        
        $env:GIT_AUTHOR_DATE = $dateStr
        $env:GIT_COMMITTER_DATE = $dateStr
        
        git commit -m "$($topic.msg)" --quiet
        $commitCount++
    }
    $currentDate = $currentDate.AddDays(1)
}

Write-Host "Successfully generated $commitCount commits!"
# Clear the manipulated env vars just in case
Remove-Item Env:\GIT_AUTHOR_DATE -ErrorAction SilentlyContinue
Remove-Item Env:\GIT_COMMITTER_DATE -ErrorAction SilentlyContinue
