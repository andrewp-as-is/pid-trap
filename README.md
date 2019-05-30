<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/pid-trap.svg?maxAge=3600)](https://pypi.org/project/pid-trap/)
[![](https://img.shields.io/npm/v/pid-trap.svg?maxAge=3600)](https://www.npmjs.com/package/pid-trap)
[![Travis](https://api.travis-ci.org/looking-for-a-job/pid-trap.svg?branch=master)](https://travis-ci.org/looking-for-a-job/pid-trap/)

#### Installation
```bash
$ [sudo] npm i -g pid-trap
```
```bash
$ [sudo] pip install pid-trap
```

#### Scripts usage
command|`usage`
-|-
`pid-trap` |`usage: pid-trap pid command [args ...]`

#### Examples
```bash
sleep 5 &
pid-trap $! echo beep
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>