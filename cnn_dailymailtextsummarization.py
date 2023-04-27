{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/karandomguy/iriscnn-dailymailsummariser/blob/tests/cnn_dailymailtextsummarization.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "s99c0_63POwR"
      },
      "outputs": [],
      "source": [
        "import numpy as np \n",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Installing dataset from Kaggle"
      ],
      "metadata": {
        "id": "Ld8kbMA6W_Kf"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cwlCIIDsPc1f",
        "outputId": "767cda9b-464a-4a42-ed4c-9f9a5c32d6d4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: kaggle in /usr/local/lib/python3.9/dist-packages (1.5.13)\n",
            "Requirement already satisfied: python-slugify in /usr/local/lib/python3.9/dist-packages (from kaggle) (8.0.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.9/dist-packages (from kaggle) (2022.12.7)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.9/dist-packages (from kaggle) (2.8.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from kaggle) (2.27.1)\n",
            "Requirement already satisfied: urllib3 in /usr/local/lib/python3.9/dist-packages (from kaggle) (1.26.15)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.9/dist-packages (from kaggle) (4.65.0)\n",
            "Requirement already satisfied: six>=1.10 in /usr/local/lib/python3.9/dist-packages (from kaggle) (1.16.0)\n",
            "Requirement already satisfied: text-unidecode>=1.3 in /usr/local/lib/python3.9/dist-packages (from python-slugify->kaggle) (1.3)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.9/dist-packages (from requests->kaggle) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->kaggle) (3.4)\n"
          ]
        }
      ],
      "source": [
        "!pip install kaggle"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0FtN7ChDQGHz",
        "outputId": "e0f019b5-108a-4f78-e529-d3b1ba540c04"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "mkdir: cannot create directory ‘/root/.kaggle’: File exists\n"
          ]
        }
      ],
      "source": [
        "!mkdir ~/.kaggle"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QrxFsWPcQmzR"
      },
      "outputs": [],
      "source": [
        "!cp kaggle.json ~/.kaggle/"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Mnma081HQr8-"
      },
      "outputs": [],
      "source": [
        "!chmod 600 ~/.kaggle/kaggle.json"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bageb3DXQwZ4",
        "outputId": "7f2a33ab-8a85-46c5-b825-c5a80e5550b4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "newspaper-text-summarization-cnn-dailymail.zip: Skipping, found more recently modified local copy (use --force to force download)\n"
          ]
        }
      ],
      "source": [
        "!kaggle datasets download -d gowrishankarp/newspaper-text-summarization-cnn-dailymail\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1C2B9CIEQ93z",
        "outputId": "5867c540-b070-4e53-bb4e-2954064d3742"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Archive:  newspaper-text-summarization-cnn-dailymail.zip\n",
            "replace cnn_dailymail/test.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: n\n",
            "replace cnn_dailymail/train.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: n\n",
            "replace cnn_dailymail/validation.csv? [y]es, [n]o, [A]ll, [N]one, [r]ename: n\n"
          ]
        }
      ],
      "source": [
        "! unzip newspaper-text-summarization-cnn-dailymail.zip"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "wER4xwCVRnXx",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 572
        },
        "outputId": "9f27e42f-181d-4f9d-f8bb-42f618ca474a"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                              id  \\\n",
              "0       0001d1afc246a7964130f43ae940af6bc6c57f01   \n",
              "1       0002095e55fcbd3a2f366d9bf92a95433dc305ef   \n",
              "2       00027e965c8264c35cc1bc55556db388da82b07f   \n",
              "3       0002c17436637c4fe1837c935c04de47adb18e9a   \n",
              "4       0003ad6ef0c37534f80b55b4235108024b407f0b   \n",
              "...                                          ...   \n",
              "287108  fffdfb56fdf1a12d364562cc2b9b1d4de7481dee   \n",
              "287109  fffeecb8690b85de8c3faed80adbc7a978f9ae2a   \n",
              "287110  ffff5231e4c71544bc6c97015cdb16c60e42b3f4   \n",
              "287111  ffff924b14a8d82058b6c1c5368ff1113c1632af   \n",
              "287112  ffffd563a96104f5cf4493cfa701a65f31b06abf   \n",
              "\n",
              "                                                  article  \\\n",
              "0       By . Associated Press . PUBLISHED: . 14:11 EST...   \n",
              "1       (CNN) -- Ralph Mata was an internal affairs li...   \n",
              "2       A drunk driver who killed a young woman in a h...   \n",
              "3       (CNN) -- With a breezy sweep of his pen Presid...   \n",
              "4       Fleetwood are the only team still to have a 10...   \n",
              "...                                                   ...   \n",
              "287108  By . James Rush . Former first daughter Chelse...   \n",
              "287109  An apologetic Vanilla Ice has given his first ...   \n",
              "287110  America's most lethal sniper claimed he wished...   \n",
              "287111  By . Sara Malm . PUBLISHED: . 12:19 EST, 8 Mar...   \n",
              "287112  (CNN)Former Florida Gov. Jeb Bush has decided ...   \n",
              "\n",
              "                                               highlights  \n",
              "0       Bishop John Folda, of North Dakota, is taking ...  \n",
              "1       Criminal complaint: Cop used his role to help ...  \n",
              "2       Craig Eccleston-Todd, 27, had drunk at least t...  \n",
              "3       Nina dos Santos says Europe must be ready to a...  \n",
              "4       Fleetwood top of League One after 2-0 win at S...  \n",
              "...                                                   ...  \n",
              "287108  Chelsea Clinton said question of running for o...  \n",
              "287109  Vanilla Ice, 47 - real name Robert Van Winkle ...  \n",
              "287110  America's most lethal sniper made comment in i...  \n",
              "287111  A swarm of more than one million has crossed b...  \n",
              "287112  Other 2016 hopefuls maintain that Bush's annou...  \n",
              "\n",
              "[287113 rows x 3 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-0654e060-073a-414f-a909-f7760c9d0944\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>article</th>\n",
              "      <th>highlights</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0001d1afc246a7964130f43ae940af6bc6c57f01</td>\n",
              "      <td>By . Associated Press . PUBLISHED: . 14:11 EST...</td>\n",
              "      <td>Bishop John Folda, of North Dakota, is taking ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0002095e55fcbd3a2f366d9bf92a95433dc305ef</td>\n",
              "      <td>(CNN) -- Ralph Mata was an internal affairs li...</td>\n",
              "      <td>Criminal complaint: Cop used his role to help ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>00027e965c8264c35cc1bc55556db388da82b07f</td>\n",
              "      <td>A drunk driver who killed a young woman in a h...</td>\n",
              "      <td>Craig Eccleston-Todd, 27, had drunk at least t...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0002c17436637c4fe1837c935c04de47adb18e9a</td>\n",
              "      <td>(CNN) -- With a breezy sweep of his pen Presid...</td>\n",
              "      <td>Nina dos Santos says Europe must be ready to a...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0003ad6ef0c37534f80b55b4235108024b407f0b</td>\n",
              "      <td>Fleetwood are the only team still to have a 10...</td>\n",
              "      <td>Fleetwood top of League One after 2-0 win at S...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>287108</th>\n",
              "      <td>fffdfb56fdf1a12d364562cc2b9b1d4de7481dee</td>\n",
              "      <td>By . James Rush . Former first daughter Chelse...</td>\n",
              "      <td>Chelsea Clinton said question of running for o...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>287109</th>\n",
              "      <td>fffeecb8690b85de8c3faed80adbc7a978f9ae2a</td>\n",
              "      <td>An apologetic Vanilla Ice has given his first ...</td>\n",
              "      <td>Vanilla Ice, 47 - real name Robert Van Winkle ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>287110</th>\n",
              "      <td>ffff5231e4c71544bc6c97015cdb16c60e42b3f4</td>\n",
              "      <td>America's most lethal sniper claimed he wished...</td>\n",
              "      <td>America's most lethal sniper made comment in i...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>287111</th>\n",
              "      <td>ffff924b14a8d82058b6c1c5368ff1113c1632af</td>\n",
              "      <td>By . Sara Malm . PUBLISHED: . 12:19 EST, 8 Mar...</td>\n",
              "      <td>A swarm of more than one million has crossed b...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>287112</th>\n",
              "      <td>ffffd563a96104f5cf4493cfa701a65f31b06abf</td>\n",
              "      <td>(CNN)Former Florida Gov. Jeb Bush has decided ...</td>\n",
              "      <td>Other 2016 hopefuls maintain that Bush's annou...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>287113 rows × 3 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0654e060-073a-414f-a909-f7760c9d0944')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-0654e060-073a-414f-a909-f7760c9d0944 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-0654e060-073a-414f-a909-f7760c9d0944');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "train_df = pd.read_csv('cnn_dailymail/train.csv')\n",
        "train_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Pz1yUT5VtH1a"
      },
      "outputs": [],
      "source": [
        "test_data = pd.read_csv('cnn_dailymail/test.csv')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tb2VzlinR0Wn"
      },
      "outputs": [],
      "source": [
        "train_df = train_df.drop(['id'],axis=1) # dropping id column"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8XkkSCtHR8-2"
      },
      "outputs": [],
      "source": [
        "train_data=train_df"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BHtqtDQ6tmPW"
      },
      "outputs": [],
      "source": [
        "train_data = train_data.reset_index(drop=True)\n",
        "test_data = test_data.drop(['id'], axis=1)\n",
        "test_data = test_data.reset_index(drop=True)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Extractive Summarization using BERT**\n",
        "\n"
      ],
      "metadata": {
        "id": "170TrJ_dRTe2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from summarizer import Summarizer\n",
        "from pprint import pprint"
      ],
      "metadata": {
        "id": "NjDx4vPYWV80"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install transformers\n",
        "!pip install spacy-transformers"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BKBuU3EBiZOd",
        "outputId": "d43334ac-bf99-4604-c464-c2dbc58b4862"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: transformers in /usr/local/lib/python3.9/dist-packages (4.28.1)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.9/dist-packages (from transformers) (23.1)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.9/dist-packages (from transformers) (2017.4.5)\n",
            "Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.9/dist-packages (from transformers) (1.22.4)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.9/dist-packages (from transformers) (4.65.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from transformers) (2.27.1)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.9/dist-packages (from transformers) (3.12.0)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.9/dist-packages (from transformers) (6.0)\n",
            "Requirement already satisfied: tokenizers!=0.11.3,<0.14,>=0.11.1 in /usr/local/lib/python3.9/dist-packages (from transformers) (0.13.3)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.11.0 in /usr/local/lib/python3.9/dist-packages (from transformers) (0.14.1)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.9/dist-packages (from huggingface-hub<1.0,>=0.11.0->transformers) (4.5.0)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.9/dist-packages (from huggingface-hub<1.0,>=0.11.0->transformers) (2023.4.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests->transformers) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests->transformers) (2022.12.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->transformers) (3.4)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.9/dist-packages (from requests->transformers) (2.0.12)\n",
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: spacy-transformers in /usr/local/lib/python3.9/dist-packages (1.2.3)\n",
            "Requirement already satisfied: numpy>=1.15.0 in /usr/local/lib/python3.9/dist-packages (from spacy-transformers) (1.22.4)\n",
            "Requirement already satisfied: transformers<4.29.0,>=3.4.0 in /usr/local/lib/python3.9/dist-packages (from spacy-transformers) (4.28.1)\n",
            "Requirement already satisfied: torch>=1.8.0 in /usr/local/lib/python3.9/dist-packages (from spacy-transformers) (2.0.0+cu118)\n",
            "Requirement already satisfied: spacy-alignments<1.0.0,>=0.7.2 in /usr/local/lib/python3.9/dist-packages (from spacy-transformers) (0.9.0)\n",
            "Requirement already satisfied: srsly<3.0.0,>=2.4.0 in /usr/local/lib/python3.9/dist-packages (from spacy-transformers) (2.4.6)\n",
            "Requirement already satisfied: spacy<4.0.0,>=3.5.0 in /usr/local/lib/python3.9/dist-packages (from spacy-transformers) (3.5.2)\n",
            "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (1.1.1)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (23.1)\n",
            "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (3.0.12)\n",
            "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (3.0.8)\n",
            "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (3.3.0)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (2.27.1)\n",
            "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<1.11.0,>=1.7.4 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (1.10.7)\n",
            "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (2.0.8)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (3.1.2)\n",
            "Requirement already satisfied: thinc<8.2.0,>=8.1.8 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (8.1.9)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (67.7.2)\n",
            "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (1.0.9)\n",
            "Requirement already satisfied: typer<0.8.0,>=0.3.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (0.7.0)\n",
            "Requirement already satisfied: smart-open<7.0.0,>=5.2.1 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (6.3.0)\n",
            "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (1.0.4)\n",
            "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (4.65.0)\n",
            "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (2.0.7)\n",
            "Requirement already satisfied: pathy>=0.10.0 in /usr/local/lib/python3.9/dist-packages (from spacy<4.0.0,>=3.5.0->spacy-transformers) (0.10.1)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.9/dist-packages (from torch>=1.8.0->spacy-transformers) (1.11.1)\n",
            "Requirement already satisfied: triton==2.0.0 in /usr/local/lib/python3.9/dist-packages (from torch>=1.8.0->spacy-transformers) (2.0.0)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.9/dist-packages (from torch>=1.8.0->spacy-transformers) (4.5.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.9/dist-packages (from torch>=1.8.0->spacy-transformers) (3.12.0)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.9/dist-packages (from torch>=1.8.0->spacy-transformers) (3.1)\n",
            "Requirement already satisfied: lit in /usr/local/lib/python3.9/dist-packages (from triton==2.0.0->torch>=1.8.0->spacy-transformers) (16.0.2)\n",
            "Requirement already satisfied: cmake in /usr/local/lib/python3.9/dist-packages (from triton==2.0.0->torch>=1.8.0->spacy-transformers) (3.25.2)\n",
            "Requirement already satisfied: tokenizers!=0.11.3,<0.14,>=0.11.1 in /usr/local/lib/python3.9/dist-packages (from transformers<4.29.0,>=3.4.0->spacy-transformers) (0.13.3)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.11.0 in /usr/local/lib/python3.9/dist-packages (from transformers<4.29.0,>=3.4.0->spacy-transformers) (0.14.1)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.9/dist-packages (from transformers<4.29.0,>=3.4.0->spacy-transformers) (6.0)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.9/dist-packages (from transformers<4.29.0,>=3.4.0->spacy-transformers) (2017.4.5)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.9/dist-packages (from huggingface-hub<1.0,>=0.11.0->transformers<4.29.0,>=3.4.0->spacy-transformers) (2023.4.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.5.0->spacy-transformers) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.9/dist-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.5.0->spacy-transformers) (2022.12.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.5.0->spacy-transformers) (3.4)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.9/dist-packages (from requests<3.0.0,>=2.13.0->spacy<4.0.0,>=3.5.0->spacy-transformers) (2.0.12)\n",
            "Requirement already satisfied: blis<0.8.0,>=0.7.8 in /usr/local/lib/python3.9/dist-packages (from thinc<8.2.0,>=8.1.8->spacy<4.0.0,>=3.5.0->spacy-transformers) (0.7.9)\n",
            "Requirement already satisfied: confection<1.0.0,>=0.0.1 in /usr/local/lib/python3.9/dist-packages (from thinc<8.2.0,>=8.1.8->spacy<4.0.0,>=3.5.0->spacy-transformers) (0.0.4)\n",
            "Requirement already satisfied: click<9.0.0,>=7.1.1 in /usr/local/lib/python3.9/dist-packages (from typer<0.8.0,>=0.3.0->spacy<4.0.0,>=3.5.0->spacy-transformers) (8.1.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.9/dist-packages (from jinja2->spacy<4.0.0,>=3.5.0->spacy-transformers) (2.1.2)\n",
            "Requirement already satisfied: mpmath>=0.19 in /usr/local/lib/python3.9/dist-packages (from sympy->torch>=1.8.0->spacy-transformers) (1.3.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train_check=train_data[1:5]"
      ],
      "metadata": {
        "id": "EORMCbWdvhHC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_check"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 175
        },
        "id": "dTX-oovtvmPZ",
        "outputId": "346a1846-1ebd-49fb-ab60-d34d1022d461"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                                             article  \\\n",
              "1  (CNN) -- Ralph Mata was an internal affairs li...   \n",
              "2  A drunk driver who killed a young woman in a h...   \n",
              "3  (CNN) -- With a breezy sweep of his pen Presid...   \n",
              "4  Fleetwood are the only team still to have a 10...   \n",
              "\n",
              "                                          highlights  \n",
              "1  Criminal complaint: Cop used his role to help ...  \n",
              "2  Craig Eccleston-Todd, 27, had drunk at least t...  \n",
              "3  Nina dos Santos says Europe must be ready to a...  \n",
              "4  Fleetwood top of League One after 2-0 win at S...  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-029d885e-1cde-48e9-a0df-32b2b2a90ada\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>article</th>\n",
              "      <th>highlights</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>(CNN) -- Ralph Mata was an internal affairs li...</td>\n",
              "      <td>Criminal complaint: Cop used his role to help ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>A drunk driver who killed a young woman in a h...</td>\n",
              "      <td>Craig Eccleston-Todd, 27, had drunk at least t...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>(CNN) -- With a breezy sweep of his pen Presid...</td>\n",
              "      <td>Nina dos Santos says Europe must be ready to a...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Fleetwood are the only team still to have a 10...</td>\n",
              "      <td>Fleetwood top of League One after 2-0 win at S...</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-029d885e-1cde-48e9-a0df-32b2b2a90ada')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-029d885e-1cde-48e9-a0df-32b2b2a90ada button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-029d885e-1cde-48e9-a0df-32b2b2a90ada');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from transformers import pipelines"
      ],
      "metadata": {
        "id": "TWoQc0vEXKNX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "!pip install rouge-score"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d9nho3yFw-pF",
        "outputId": "c5420798-7e29-4906-8503-2d2573fce0f0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: rouge-score in /usr/local/lib/python3.9/dist-packages (0.1.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.9/dist-packages (from rouge-score) (1.22.4)\n",
            "Requirement already satisfied: nltk in /usr/local/lib/python3.9/dist-packages (from rouge-score) (3.8.1)\n",
            "Requirement already satisfied: absl-py in /usr/local/lib/python3.9/dist-packages (from rouge-score) (1.4.0)\n",
            "Requirement already satisfied: six>=1.14.0 in /usr/local/lib/python3.9/dist-packages (from rouge-score) (1.16.0)\n",
            "Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.9/dist-packages (from nltk->rouge-score) (2023.3.23)\n",
            "Requirement already satisfied: click in /usr/local/lib/python3.9/dist-packages (from nltk->rouge-score) (8.1.3)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.9/dist-packages (from nltk->rouge-score) (4.65.0)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.9/dist-packages (from nltk->rouge-score) (1.2.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Example 1\n"
      ],
      "metadata": {
        "id": "GKcLk5DMS2LI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "summarizer = pipeline(\"summarization\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 233,
          "referenced_widgets": [
            "919390b4a6c349618423e7c44c2fdff2",
            "8d558af7c01148c9a342042a3e5670d1",
            "ee9e862e87ba4dcba602fc7b9348ae69",
            "1ac3c04894604c71bc799c4912b70620",
            "57406be6b135499bbc5185ebbe1366b3",
            "83c4d214e1f041618c8a5ec569d36a14",
            "e7bc3040099349bea77851293932a2f9",
            "2e06f92c2312405baf95a43300bf1901",
            "37501722577441f29b70e85cf2eee0e3",
            "6555897fd5a6442982809c29592ecdc9",
            "67b325ad412d4c3492cbcf310ba11b23",
            "c178d64ffdbc46fd82b215da1d11013d",
            "85ad276e2b46400e8ed9c3deb59831f4",
            "a53c84968dd14405afa35818b554378a",
            "0de414a6ea81456f8870f1b8922d41b4",
            "09ae555582184ea9bf4428b1314cdb1f",
            "4ede8ddadc954f45ab860c1ebd1674ef",
            "e2ddd5134c1d4c4f94f5821715b57d2e",
            "030b1745a2b04ae99174105146de5e2c",
            "1df2cc2787f7480fb12e67e494b829fd",
            "b7f38790dae14cbb9b05f1bc25ad4668",
            "a1df438adfbf4011a66c3d1f7192b505",
            "a9b0cdf6317642139f94382bcaa55d2a",
            "e6f89bd421674b83bc92296124f2222b",
            "f50a738528b8419aaa42143344fd17c1",
            "3b03c252f797406abd5f4a2aebf8a363",
            "50d284a1c9bf4f9eaf480ee2baa287ba",
            "018feeb5e2a547e0bcb028fa5fbf1133",
            "96813de3050a46f785a708cbd3965d93",
            "e637daf385a64f83b8ab82bcb9130a1a",
            "d67aefbc9a1047d1b3de993cc1e4f02e",
            "dca930bc7d52439aace30c142f99ce05",
            "a2732af9856b4a6384a0e36c156d3378",
            "a91a66b5475f4b159d0afc0b40e2819e",
            "1ae3fddfd9a2488f8f26715ce41a9071",
            "253b586d65d049d89ce46812adc39176",
            "d13b8c193dc745ef9ba551b4bc44be5c",
            "f6eeab63d44f42099d5b5fcb51877d64",
            "7b5274cd2cf947408ed00c94256196d9",
            "72c27ce6a6b84bd69e308edeeae24161",
            "0adaa5f3c6c64f6b908b29fc8e3a2de9",
            "701b42f7fa3c47e7b7be1509b9fb3781",
            "00d457c5d8a64f0a8ba867e8c8e3c05e",
            "18fac98203194ea6a35117fe0dfdda4f",
            "75105d9de1c74fd1bb622dde94b0e4e9",
            "a89e5a0b2fcc4b4aa85bd9234862daef",
            "140f89a14eff4fdcb1bcae695fd812ad",
            "d2abcb9695724867bdea665ad4bb170b",
            "7f9ce284dde7459f9570763e47ed0a32",
            "17c369d6b64344b78566bd243508c264",
            "475a60aada19477db8fdbcbf5b6b0f2d",
            "e765e6a45f664d8fb9763058298034e5",
            "e849b7abb46a44a3a59a84132fef5bb7",
            "849013d0cc2744518abdb1db75a179fd",
            "b6146b3a31b94288abdd6eaebf3736f1"
          ]
        },
        "id": "chNailXm-3FI",
        "outputId": "f86f92e2-9178-4df4-d778-6da25c67c91f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "No model was supplied, defaulted to sshleifer/distilbart-cnn-12-6 and revision a4f8f3e (https://huggingface.co/sshleifer/distilbart-cnn-12-6).\n",
            "Using a pipeline without specifying a model name and revision in production is not recommended.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Downloading (…)lve/main/config.json:   0%|          | 0.00/1.80k [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "919390b4a6c349618423e7c44c2fdff2"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Downloading pytorch_model.bin:   0%|          | 0.00/1.22G [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "c178d64ffdbc46fd82b215da1d11013d"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Downloading (…)okenizer_config.json:   0%|          | 0.00/26.0 [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "a9b0cdf6317642139f94382bcaa55d2a"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Downloading (…)olve/main/vocab.json:   0%|          | 0.00/899k [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "a91a66b5475f4b159d0afc0b40e2819e"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Downloading (…)olve/main/merges.txt:   0%|          | 0.00/456k [00:00<?, ?B/s]"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "75105d9de1c74fd1bb622dde94b0e4e9"
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ARTICLE=train_check['article'][2]\n",
        "ARTICLE = ARTICLE.replace('.', '.<eos>')\n",
        "ARTICLE = ARTICLE.replace('?', '?<eos>')\n",
        "ARTICLE = ARTICLE.replace('!', '!<eos>')"
      ],
      "metadata": {
        "id": "d7PKoa4Y-5VO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "max_chunk = 500\n",
        "sentences = ARTICLE.split('<eos>')\n",
        "current_chunk = 0 \n",
        "chunks = []\n",
        "for sentence in sentences:\n",
        "    if len(chunks) == current_chunk + 1: \n",
        "        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:\n",
        "            chunks[current_chunk].extend(sentence.split(' '))\n",
        "        else:\n",
        "            current_chunk += 1\n",
        "            chunks.append(sentence.split(' '))\n",
        "    else:\n",
        "        print(current_chunk)\n",
        "        chunks.append(sentence.split(' '))\n",
        "\n",
        "for chunk_id in range(len(chunks)):\n",
        "    chunks[chunk_id] = ' '.join(chunks[chunk_id])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lucCsr2F_SvE",
        "outputId": "23d8344e-4497-45d2-cf89-b90624f1cfe1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)"
      ],
      "metadata": {
        "id": "HCIEhhLaCRQs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "output=str(res[0])"
      ],
      "metadata": {
        "id": "75eknCi0CTxR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_check['highlights'][2]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 89
        },
        "id": "fc2SghyfCkTT",
        "outputId": "f1409d2e-2f40-45fe-8d82-6dce46e54a63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"Craig Eccleston-Todd, 27, had drunk at least three pints before driving car .\\nWas using phone when he veered across road in Yarmouth, Isle of Wight .\\nCrashed head-on into 28-year-old Rachel Titley's car, who died in hospital .\\nPolice say he would have been over legal drink-drive limit at time of crash .\\nHe was found guilty at Portsmouth Crown Court of causing death by dangerous driving .\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 90
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from rouge_score import rouge_scorer\n",
        "scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)\n",
        "scores = scorer.score(output,\n",
        "                      train_check['highlights'][2])"
      ],
      "metadata": {
        "id": "1xe_k8FoCYBF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "scores"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gbEJ6dTiCek5",
        "outputId": "c7cf65e8-d2d7-4aeb-ae10-f2de4ff9f346"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'rouge1': Score(precision=0.5142857142857142, recall=0.5, fmeasure=0.5070422535211268),\n",
              " 'rougeL': Score(precision=0.2857142857142857, recall=0.2777777777777778, fmeasure=0.28169014084507044)}"
            ]
          },
          "metadata": {},
          "execution_count": 92
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Example 2"
      ],
      "metadata": {
        "id": "8zzbbFcWTDF8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ARTICLE2=train_check['article'][3]\n",
        "ARTICLE2 = ARTICLE2.replace('.', '.<eos>')\n",
        "ARTICLE2 = ARTICLE2.replace('?', '?<eos>')\n",
        "ARTICLE2 = ARTICLE2.replace('!', '!<eos>')"
      ],
      "metadata": {
        "id": "LhzImuNhDlfI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "max_chunk = 500\n",
        "sentences = ARTICLE2.split('<eos>')\n",
        "current_chunk = 0 \n",
        "chunks = []\n",
        "for sentence in sentences:\n",
        "    if len(chunks) == current_chunk + 1: \n",
        "        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:\n",
        "            chunks[current_chunk].extend(sentence.split(' '))\n",
        "        else:\n",
        "            current_chunk += 1\n",
        "            chunks.append(sentence.split(' '))\n",
        "    else:\n",
        "        print(current_chunk)\n",
        "        chunks.append(sentence.split(' '))\n",
        "\n",
        "for chunk_id in range(len(chunks)):\n",
        "    chunks[chunk_id] = ' '.join(chunks[chunk_id])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rzXEO3SMTILN",
        "outputId": "daa4956e-6c62-40e4-d01f-2efbadcc9efd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rF4H5k_YTRC5",
        "outputId": "55d5ef96-4977-4706-fd64-5ba2b73093a9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Your max_length is set to 120, but you input_length is only 68. You might consider decreasing max_length manually, e.g. summarizer('...', max_length=34)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "output2=str(res[0])"
      ],
      "metadata": {
        "id": "FPHmZ03gTR76"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_check['highlights'][3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 71
        },
        "id": "-obeWxe8TVti",
        "outputId": "da21dd20-cb4f-4f2f-f334-6be040f946e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"Nina dos Santos says Europe must be ready to accept sanctions will hurt both sides .\\nTargeting Russia's business community would be one way of sapping their support for President Putin, she says .\\nBut she says Europe would have a hard time keeping its factories going without power from the east .\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 97
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from rouge_score import rouge_scorer\n",
        "scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)\n",
        "scores = scorer.score(output2,\n",
        "                      train_check['highlights'][3])"
      ],
      "metadata": {
        "id": "V06xwRitTYVx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "scores"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "du5-JqBOTb9b",
        "outputId": "faaefd1b-09ae-4a77-e64a-1e414fb9941a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'rouge1': Score(precision=0.3333333333333333, recall=0.25757575757575757, fmeasure=0.2905982905982906),\n",
              " 'rougeL': Score(precision=0.17647058823529413, recall=0.13636363636363635, fmeasure=0.15384615384615383)}"
            ]
          },
          "metadata": {},
          "execution_count": 99
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Example 3"
      ],
      "metadata": {
        "id": "svpKTcurTkwJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ARTICLE3=train_check['article'][4]\n",
        "ARTICLE3 = ARTICLE3.replace('.', '.<eos>')\n",
        "ARTICLE3 = ARTICLE3.replace('?', '?<eos>')\n",
        "ARTICLE3 = ARTICLE3.replace('!', '!<eos>')"
      ],
      "metadata": {
        "id": "2N-foaoeTc-v"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "max_chunk = 500\n",
        "sentences = ARTICLE3.split('<eos>')\n",
        "current_chunk = 0 \n",
        "chunks = []\n",
        "for sentence in sentences:\n",
        "    if len(chunks) == current_chunk + 1: \n",
        "        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:\n",
        "            chunks[current_chunk].extend(sentence.split(' '))\n",
        "        else:\n",
        "            current_chunk += 1\n",
        "            chunks.append(sentence.split(' '))\n",
        "    else:\n",
        "        print(current_chunk)\n",
        "        chunks.append(sentence.split(' '))\n",
        "\n",
        "for chunk_id in range(len(chunks)):\n",
        "    chunks[chunk_id] = ' '.join(chunks[chunk_id])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JXjOo8TmTrtG",
        "outputId": "f21cb3f0-46d4-4fff-efbf-49e13fae5cb2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)"
      ],
      "metadata": {
        "id": "jqJKRq7zTvA4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "output3=str(res[0])"
      ],
      "metadata": {
        "id": "EW_MYd_nTx0X"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_check['highlights'][4]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 89
        },
        "id": "ueP8-vQUT0Pn",
        "outputId": "344a7c67-4cb4-4231-b679-f98e89265cbd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Fleetwood top of League One after 2-0 win at Scunthorpe .\\nPeterborough, Bristol City, Chesterfield and Crawley all drop first points of the season .\\nStand-in striker Matt Done scores a hat-trick as Rochdale thrash Crewe 5-2 .\\nWins for Notts County and Yeovil .\\nCoventry/Bradford and Oldham/Port Vale both end in draws .\\nA late Stephen Bywater own goal denies Gillingham three points against Millwall .'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 104
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "output3"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 89
        },
        "id": "wifswapQUH-l",
        "outputId": "1b87e005-eb4d-4ded-afd4-1d0c70699288"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"{'summary_text': ' fleetwood are the only team still to have a 100% record in sky bet league one . graham alexander’s men beat scunthorpe 2-0 to go top of the table . posh were defeated 2-1 by sheffield united, who had lost both of their opening games . bristol city were held to a goalless draw by leyton orient . crawley lost their unbeaten status, while bradford maintained theirs thanks to a 3-1 win for the bantams .'}\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 107
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train_check['article'][4]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 178
        },
        "id": "gO4EOHFeXwsg",
        "outputId": "a2a86173-6eed-4406-f94f-1a1330daffb6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"fleetwood are the only team still to have a 100% record in sky bet league one as a 2-0 win over scunthorpe sent graham alexander’s men top of the table. the cod army are playing in the third tier for the first time in their history after six promotions in nine years and their remarkable ascent shows no sign of slowing with jamie proctor and gareth evans scoring the goals at glanford park. fleetwood were one of five teams to have won two out of two but the other four clubs - peterborough, bristol city, chesterfield and crawley - all hit their first stumbling blocks. posh were defeated 2-1 by sheffield united, who had lost both of their opening contests. jose baxter’s opener gave the blades a first-half lead, and although it was later cancelled out by shaun brisley’s goal, ben davies snatched a winner six minutes from time. in the lead: jose baxter (right) celebrates opening the scoring for sheffield united . up for the battle: sheffield united's michael doyle (left) challenges peterborough's kyle vassell in a keenly-contested clash . bristol city, who beat nigel clough’s men on the opening day, were held to a goalless draw by last season's play-off finalists leyton orient while chesterfield, the league two champions, were beaten 1-0 by mk dons, who play manchester united in the capital one cup in seven days’ time. arsenal loanee benik afobe scored the only goal of the game just after the break. meanwhile, crawley lost their unbeaten status, while bradford maintained theirs, thanks to a 3-1 win for the bantams. james hanson became the first player to score against crawley this season after 49 minutes before joe walsh equalised five minutes later. heads up: bristol city's korey smith (left) and leyton orient's lloyd james go up for a header . but strikes from billy knott and mason bennett sealed an impressive away win phil parkinson's men. bradford are now second behind fleetwood after doncaster’s stoppage-time equaliser meant preston, for whom joe garner signed a new contract earlier on tuesday, were held to a 1-1 draw which slipped them down the table. chris humphrey looked to have secured the points for the lilywhites but nathan tyson struck a last-gasp leveller. stand-in striker matt done scored a hat-trick for rochdale in the evening’s high-scoring affair as crewe were hammered 5-2. marcus haber marked his full railwaymen debut with a brace but done’s treble and goals from ian henderson and peter vincenti helped keith hill’s men to a big away victory. there were plenty of goals between coventry and barnsley too in a 2-2 draw with all four goals coming in the first half. josh mcquoid and jordan clarke twice gave the sky blues the lead, but the tykes earned a point thanks to strikes from conor hourihane and leroy lita. notts county recorded a 2-1 home win over colchester with ronan murray and liam noble on target. freddie sears replied for colchester. james wilson's second half equaliser earned oldham a points against port vale after tom pope's opener and yeovil claimed a 2-1 away victory at walsall with kevin dawson striking a late winner. tom bradshaw had equalised after veteran james hayter gave the glovers the lead. finally, swindon held gillingham to a 2-2 draw thanks to stephen bywater’s last-minute own goal. danny kedwell and kortney hause twice gave the gills the lead but andy williams pulled swindon level before bywater dropped raphael branco's cross into his own net.\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 129
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from rouge_score import rouge_scorer\n",
        "scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)\n",
        "scores = scorer.score(output3,\n",
        "                      train_check['highlights'][4])"
      ],
      "metadata": {
        "id": "4ZXVElFIT22K"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "scores"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FhvWmsG9T6Pq",
        "outputId": "da5d15cd-1d2f-4957-ac51-d5d68c83d7c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'rouge1': Score(precision=0.3283582089552239, recall=0.2857142857142857, fmeasure=0.3055555555555556),\n",
              " 'rougeL': Score(precision=0.16417910447761194, recall=0.14285714285714285, fmeasure=0.1527777777777778)}"
            ]
          },
          "metadata": {},
          "execution_count": 106
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Example 4\n",
        "\n"
      ],
      "metadata": {
        "id": "ISSEfBmQUO_O"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ARTICLE4=train_data['article'][5]\n",
        "ARTICLE4 = ARTICLE4.replace('.', '.<eos>')\n",
        "ARTICLE4 = ARTICLE4.replace('?', '?<eos>')\n",
        "ARTICLE4 = ARTICLE4.replace('!', '!<eos>')"
      ],
      "metadata": {
        "id": "uwAWm9N0UB9L"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "max_chunk = 500\n",
        "sentences = ARTICLE4.split('<eos>')\n",
        "current_chunk = 0 \n",
        "chunks = []\n",
        "for sentence in sentences:\n",
        "    if len(chunks) == current_chunk + 1: \n",
        "        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:\n",
        "            chunks[current_chunk].extend(sentence.split(' '))\n",
        "        else:\n",
        "            current_chunk += 1\n",
        "            chunks.append(sentence.split(' '))\n",
        "    else:\n",
        "        print(current_chunk)\n",
        "        chunks.append(sentence.split(' '))\n",
        "\n",
        "for chunk_id in range(len(chunks)):\n",
        "    chunks[chunk_id] = ' '.join(chunks[chunk_id])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xK3_ah_BUYfP",
        "outputId": "4ab08e6a-e4f9-4f6b-892f-54100868ef7c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)"
      ],
      "metadata": {
        "id": "QU9UgMQfU1HX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "output4=str(res[0])"
      ],
      "metadata": {
        "id": "148LTMeeVAJh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_data['highlights'][5]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "h0SLWI2AVDig",
        "outputId": "bef5fdcc-7b43-4761-ddd8-2432cab2ee3d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Prime Minister and his family are enjoying an Easter break in Lanzarote .\\nSported the same £20.99 beige loafers as he wore in Portugal last year .\\nPM sat and had a drink at a beach-side cafe on the Spanish Island .'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 113
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "output4"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 71
        },
        "id": "ziUmYIinVIX0",
        "outputId": "8417eaec-9d6d-4789-ab25-f5c40035131f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"{'summary_text': ' David Cameron was seen in the same pair of beige loafers he wore on holiday last year . He got the £20.99 shoes from high street store Aldo and took them with him to Portugal last summer . He teamed them with a navy blue shirt and beige shorts on a trip to Teguise in the centre of the island .'}\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 114
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from rouge_score import rouge_scorer\n",
        "scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)\n",
        "scores = scorer.score(output4,\n",
        "                      train_data['highlights'][5])"
      ],
      "metadata": {
        "id": "ikJLBPNFVKdf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "scores"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dsbiz2TPVYH7",
        "outputId": "4f261286-eb38-4137-9990-249e98e2f732"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'rouge1': Score(precision=0.4878048780487805, recall=0.32786885245901637, fmeasure=0.39215686274509803),\n",
              " 'rougeL': Score(precision=0.34146341463414637, recall=0.22950819672131148, fmeasure=0.27450980392156865)}"
            ]
          },
          "metadata": {},
          "execution_count": 126
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Example 5"
      ],
      "metadata": {
        "id": "XWy4m3EcVb9D"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ARTICLE5=train_data['article'][6]\n",
        "ARTICLE5 = ARTICLE5.replace('.', '.<eos>')\n",
        "ARTICLE5 = ARTICLE5.replace('?', '?<eos>')\n",
        "ARTICLE5 = ARTICLE5.replace('!', '!<eos>')"
      ],
      "metadata": {
        "id": "Odg6sLH1VYvB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "max_chunk = 500\n",
        "sentences = ARTICLE5.split('<eos>')\n",
        "current_chunk = 0 \n",
        "chunks = []\n",
        "for sentence in sentences:\n",
        "    if len(chunks) == current_chunk + 1: \n",
        "        if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:\n",
        "            chunks[current_chunk].extend(sentence.split(' '))\n",
        "        else:\n",
        "            current_chunk += 1\n",
        "            chunks.append(sentence.split(' '))\n",
        "    else:\n",
        "        print(current_chunk)\n",
        "        chunks.append(sentence.split(' '))\n",
        "\n",
        "for chunk_id in range(len(chunks)):\n",
        "    chunks[chunk_id] = ' '.join(chunks[chunk_id])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IfvtDoJuVjaw",
        "outputId": "158b10e9-2050-4b17-ed3f-33181db18964"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "res = summarizer(chunks, max_length=120, min_length=30, do_sample=False)"
      ],
      "metadata": {
        "id": "tG7SokaMVnBs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "output5=str(res[0])"
      ],
      "metadata": {
        "id": "Oc0MZHDwVo9A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_data['highlights'][6]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "8XeeWNCYVrMe",
        "outputId": "1df5eff8-e3d6-47e9-e83a-dcd55c9affb2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'NBA star calls for black and Hispanic communities to get tested .\\nFormer Lakers player dedicated life to raising awareness about disease .'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 121
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "output5"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 53
        },
        "id": "leoEotZQVuOK",
        "outputId": "ed3a46eb-5aeb-4374-e5d5-1c1329966003"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'{\\'summary_text\\': \" Magic Johnson was \\'devastated\\' when he was told he had HIV in 1991 . The former Los Angeles Lakers player is now campaigning for more people to get tested for the disease .\"}'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 123
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from rouge_score import rouge_scorer\n",
        "scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)\n",
        "scores = scorer.score(output5,\n",
        "                      train_data['highlights'][6])"
      ],
      "metadata": {
        "id": "KVKs2gkPVxYc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "scores"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xPppWWcsV8dA",
        "outputId": "496f29b6-34db-4681-ccb0-de9eafdb8655"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'rouge1': Score(precision=0.38095238095238093, recall=0.24242424242424243, fmeasure=0.2962962962962963),\n",
              " 'rougeL': Score(precision=0.23809523809523808, recall=0.15151515151515152, fmeasure=0.18518518518518517)}"
            ]
          },
          "metadata": {},
          "execution_count": 128
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Ynq__jc6WBIz"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPZAKwSGdsZna790+Xemy9y",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "919390b4a6c349618423e7c44c2fdff2": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_8d558af7c01148c9a342042a3e5670d1",
              "IPY_MODEL_ee9e862e87ba4dcba602fc7b9348ae69",
              "IPY_MODEL_1ac3c04894604c71bc799c4912b70620"
            ],
            "layout": "IPY_MODEL_57406be6b135499bbc5185ebbe1366b3"
          }
        },
        "8d558af7c01148c9a342042a3e5670d1": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_83c4d214e1f041618c8a5ec569d36a14",
            "placeholder": "​",
            "style": "IPY_MODEL_e7bc3040099349bea77851293932a2f9",
            "value": "Downloading (…)lve/main/config.json: 100%"
          }
        },
        "ee9e862e87ba4dcba602fc7b9348ae69": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatProgressModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "FloatProgressModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ProgressView",
            "bar_style": "success",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_2e06f92c2312405baf95a43300bf1901",
            "max": 1802,
            "min": 0,
            "orientation": "horizontal",
            "style": "IPY_MODEL_37501722577441f29b70e85cf2eee0e3",
            "value": 1802
          }
        },
        "1ac3c04894604c71bc799c4912b70620": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_6555897fd5a6442982809c29592ecdc9",
            "placeholder": "​",
            "style": "IPY_MODEL_67b325ad412d4c3492cbcf310ba11b23",
            "value": " 1.80k/1.80k [00:00&lt;00:00, 23.5kB/s]"
          }
        },
        "57406be6b135499bbc5185ebbe1366b3": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "83c4d214e1f041618c8a5ec569d36a14": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "e7bc3040099349bea77851293932a2f9": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "2e06f92c2312405baf95a43300bf1901": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "37501722577441f29b70e85cf2eee0e3": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ProgressStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ProgressStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "bar_color": null,
            "description_width": ""
          }
        },
        "6555897fd5a6442982809c29592ecdc9": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "67b325ad412d4c3492cbcf310ba11b23": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "c178d64ffdbc46fd82b215da1d11013d": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_85ad276e2b46400e8ed9c3deb59831f4",
              "IPY_MODEL_a53c84968dd14405afa35818b554378a",
              "IPY_MODEL_0de414a6ea81456f8870f1b8922d41b4"
            ],
            "layout": "IPY_MODEL_09ae555582184ea9bf4428b1314cdb1f"
          }
        },
        "85ad276e2b46400e8ed9c3deb59831f4": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_4ede8ddadc954f45ab860c1ebd1674ef",
            "placeholder": "​",
            "style": "IPY_MODEL_e2ddd5134c1d4c4f94f5821715b57d2e",
            "value": "Downloading pytorch_model.bin: 100%"
          }
        },
        "a53c84968dd14405afa35818b554378a": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatProgressModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "FloatProgressModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ProgressView",
            "bar_style": "success",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_030b1745a2b04ae99174105146de5e2c",
            "max": 1222317369,
            "min": 0,
            "orientation": "horizontal",
            "style": "IPY_MODEL_1df2cc2787f7480fb12e67e494b829fd",
            "value": 1222317369
          }
        },
        "0de414a6ea81456f8870f1b8922d41b4": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_b7f38790dae14cbb9b05f1bc25ad4668",
            "placeholder": "​",
            "style": "IPY_MODEL_a1df438adfbf4011a66c3d1f7192b505",
            "value": " 1.22G/1.22G [00:24&lt;00:00, 53.3MB/s]"
          }
        },
        "09ae555582184ea9bf4428b1314cdb1f": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "4ede8ddadc954f45ab860c1ebd1674ef": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "e2ddd5134c1d4c4f94f5821715b57d2e": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "030b1745a2b04ae99174105146de5e2c": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "1df2cc2787f7480fb12e67e494b829fd": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ProgressStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ProgressStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "bar_color": null,
            "description_width": ""
          }
        },
        "b7f38790dae14cbb9b05f1bc25ad4668": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "a1df438adfbf4011a66c3d1f7192b505": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "a9b0cdf6317642139f94382bcaa55d2a": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_e6f89bd421674b83bc92296124f2222b",
              "IPY_MODEL_f50a738528b8419aaa42143344fd17c1",
              "IPY_MODEL_3b03c252f797406abd5f4a2aebf8a363"
            ],
            "layout": "IPY_MODEL_50d284a1c9bf4f9eaf480ee2baa287ba"
          }
        },
        "e6f89bd421674b83bc92296124f2222b": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_018feeb5e2a547e0bcb028fa5fbf1133",
            "placeholder": "​",
            "style": "IPY_MODEL_96813de3050a46f785a708cbd3965d93",
            "value": "Downloading (…)okenizer_config.json: 100%"
          }
        },
        "f50a738528b8419aaa42143344fd17c1": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatProgressModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "FloatProgressModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ProgressView",
            "bar_style": "success",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_e637daf385a64f83b8ab82bcb9130a1a",
            "max": 26,
            "min": 0,
            "orientation": "horizontal",
            "style": "IPY_MODEL_d67aefbc9a1047d1b3de993cc1e4f02e",
            "value": 26
          }
        },
        "3b03c252f797406abd5f4a2aebf8a363": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_dca930bc7d52439aace30c142f99ce05",
            "placeholder": "​",
            "style": "IPY_MODEL_a2732af9856b4a6384a0e36c156d3378",
            "value": " 26.0/26.0 [00:00&lt;00:00, 683B/s]"
          }
        },
        "50d284a1c9bf4f9eaf480ee2baa287ba": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "018feeb5e2a547e0bcb028fa5fbf1133": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "96813de3050a46f785a708cbd3965d93": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "e637daf385a64f83b8ab82bcb9130a1a": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "d67aefbc9a1047d1b3de993cc1e4f02e": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ProgressStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ProgressStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "bar_color": null,
            "description_width": ""
          }
        },
        "dca930bc7d52439aace30c142f99ce05": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "a2732af9856b4a6384a0e36c156d3378": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "a91a66b5475f4b159d0afc0b40e2819e": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_1ae3fddfd9a2488f8f26715ce41a9071",
              "IPY_MODEL_253b586d65d049d89ce46812adc39176",
              "IPY_MODEL_d13b8c193dc745ef9ba551b4bc44be5c"
            ],
            "layout": "IPY_MODEL_f6eeab63d44f42099d5b5fcb51877d64"
          }
        },
        "1ae3fddfd9a2488f8f26715ce41a9071": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_7b5274cd2cf947408ed00c94256196d9",
            "placeholder": "​",
            "style": "IPY_MODEL_72c27ce6a6b84bd69e308edeeae24161",
            "value": "Downloading (…)olve/main/vocab.json: 100%"
          }
        },
        "253b586d65d049d89ce46812adc39176": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatProgressModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "FloatProgressModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ProgressView",
            "bar_style": "success",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_0adaa5f3c6c64f6b908b29fc8e3a2de9",
            "max": 898822,
            "min": 0,
            "orientation": "horizontal",
            "style": "IPY_MODEL_701b42f7fa3c47e7b7be1509b9fb3781",
            "value": 898822
          }
        },
        "d13b8c193dc745ef9ba551b4bc44be5c": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_00d457c5d8a64f0a8ba867e8c8e3c05e",
            "placeholder": "​",
            "style": "IPY_MODEL_18fac98203194ea6a35117fe0dfdda4f",
            "value": " 899k/899k [00:00&lt;00:00, 4.87MB/s]"
          }
        },
        "f6eeab63d44f42099d5b5fcb51877d64": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "7b5274cd2cf947408ed00c94256196d9": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "72c27ce6a6b84bd69e308edeeae24161": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "0adaa5f3c6c64f6b908b29fc8e3a2de9": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "701b42f7fa3c47e7b7be1509b9fb3781": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ProgressStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ProgressStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "bar_color": null,
            "description_width": ""
          }
        },
        "00d457c5d8a64f0a8ba867e8c8e3c05e": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "18fac98203194ea6a35117fe0dfdda4f": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "75105d9de1c74fd1bb622dde94b0e4e9": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_a89e5a0b2fcc4b4aa85bd9234862daef",
              "IPY_MODEL_140f89a14eff4fdcb1bcae695fd812ad",
              "IPY_MODEL_d2abcb9695724867bdea665ad4bb170b"
            ],
            "layout": "IPY_MODEL_7f9ce284dde7459f9570763e47ed0a32"
          }
        },
        "a89e5a0b2fcc4b4aa85bd9234862daef": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_17c369d6b64344b78566bd243508c264",
            "placeholder": "​",
            "style": "IPY_MODEL_475a60aada19477db8fdbcbf5b6b0f2d",
            "value": "Downloading (…)olve/main/merges.txt: 100%"
          }
        },
        "140f89a14eff4fdcb1bcae695fd812ad": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "FloatProgressModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "FloatProgressModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ProgressView",
            "bar_style": "success",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_e765e6a45f664d8fb9763058298034e5",
            "max": 456318,
            "min": 0,
            "orientation": "horizontal",
            "style": "IPY_MODEL_e849b7abb46a44a3a59a84132fef5bb7",
            "value": 456318
          }
        },
        "d2abcb9695724867bdea665ad4bb170b": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HTMLModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HTMLModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HTMLView",
            "description": "",
            "description_tooltip": null,
            "layout": "IPY_MODEL_849013d0cc2744518abdb1db75a179fd",
            "placeholder": "​",
            "style": "IPY_MODEL_b6146b3a31b94288abdd6eaebf3736f1",
            "value": " 456k/456k [00:00&lt;00:00, 6.15MB/s]"
          }
        },
        "7f9ce284dde7459f9570763e47ed0a32": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "17c369d6b64344b78566bd243508c264": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "475a60aada19477db8fdbcbf5b6b0f2d": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "e765e6a45f664d8fb9763058298034e5": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "e849b7abb46a44a3a59a84132fef5bb7": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ProgressStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ProgressStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "bar_color": null,
            "description_width": ""
          }
        },
        "849013d0cc2744518abdb1db75a179fd": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "b6146b3a31b94288abdd6eaebf3736f1": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        }
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}