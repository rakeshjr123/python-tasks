{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNC9B/8UJQ43rEK0F4Xfj/e",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rakeshjr123/python-tasks/blob/main/Task1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ANjqsHgBk0b8",
        "outputId": "dd042144-b4b8-4c6b-fd88-bcbc897a4924"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first number : 5\n",
            "Enter the second number : 10\n",
            "Addition: 15\n",
            "Subtraction: -5\n",
            "Multiplication: 50\n",
            "Division: 0.5\n"
          ]
        }
      ],
      "source": [
        "try:\n",
        "  inp1 =int(input(\"Enter the first number : \"))\n",
        "  inp2= int(input(\"Enter the second number : \"))\n",
        "  def additionOftwoNum(a,b):\n",
        "    print(f\"Addition: {a+b}\")\n",
        "  def DifferenceOftwoNum(a,b):\n",
        "    print(f\"Subtraction: {a-b}\")\n",
        "  def ProductOftwoNum(a,b):\n",
        "    print(f\"Multiplication: {a*b}\")\n",
        "  def DivisionOftwoNum(a,b):\n",
        "    print(f\"Division: {a/b}\")\n",
        "\n",
        "  additionOftwoNum(inp1,inp2)\n",
        "  DifferenceOftwoNum(inp1,inp2)\n",
        "  ProductOftwoNum(inp1,inp2)\n",
        "  DivisionOftwoNum(inp1,inp2)\n",
        "except:\n",
        "  print(\"invalid input,please enter numbers only\")\n",
        "\n"
      ]
    }
  ]
}