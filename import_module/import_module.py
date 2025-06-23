import flet as ft
from flet import *
import math
import os
import webbrowser
from datetime import datetime
from docx import Document
from docx.shared import Pt  # Для работы с размерами шрифта
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT  # Для выравнивания текста
from openpyxl import Workbook
from docx.shared import Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from flet.core.alignment import Alignment
from openpyxl.styles import Alignment as OpenPyXLAlignment, Border, Side
import pandas as pd
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from pathlib import Path
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
