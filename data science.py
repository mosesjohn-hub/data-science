
{
 "cells": [
  {
   "cell_type": "code",
   "id": "initial_id",
   "metadata": {
    "collapsed": true,
    "ExecuteTime": {
     "end_time": "2025-07-03T00:02:04.180938Z",
     "start_time": "2025-07-03T00:02:04.168767Z"
    }
   },
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import seaborn as sns"
   ],
   "outputs": [],
   "execution_count": 13
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-07-03T00:02:04.391403Z",
     "start_time": "2025-07-03T00:02:04.294279Z"
    }
   },
   "cell_type": "code",
   "source": "df = pd.read_csv(\"all_recs.csv\", encoding=\"latin1\")\n",
   "id": "d24e0b21b832834d",
   "outputs": [],
   "execution_count": 14
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-07-03T00:02:04.518605Z",
     "start_time": "2025-07-03T00:02:04.475812Z"
    }
   },
   "cell_type": "code",
   "source": "df.head()",
   "id": "aac4745c81ec8e1d",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "        Date                     Location  \\\n",
       "0  31/12/2022  Iran (Islamic Republic of)   \n",
       "1  31/12/2022    United States of America   \n",
       "2  30/12/2022                      Poland   \n",
       "3  30/12/2022    United States of America   \n",
       "4  30/12/2022  Iran (Islamic Republic of)   \n",
       "\n",
       "                                              Victim  \\\n",
       "0                         State-run Iranian Websites   \n",
       "1  Housing Authority of the City of Los Angeles (...   \n",
       "2                                  Polish Parliament   \n",
       "3                      CentraState Healthcare System   \n",
       "4                                      Iran Airlines   \n",
       "\n",
       "                            Industry      Actor Location            Actor  \\\n",
       "0              Public Administration        Undetermined     Undetermined   \n",
       "1              Public Administration        Undetermined      LockBit 3.0   \n",
       "2              Public Administration  Russian Federation    NoName057(16)   \n",
       "3  Health Care and Social Assistance        Undetermined     Undetermined   \n",
       "4     Transportation and Warehousing             Ukraine  rootkitsecurity   \n",
       "\n",
       "         Motive          Type                     Sub-Type  Year  \n",
       "0       Protest    Disruptive  External Denial of Services  2022  \n",
       "1     Financial  Exploitative                 Undetermined  2022  \n",
       "2       Protest    Disruptive  External Denial of Services  2022  \n",
       "3  Undetermined    Disruptive                 Undetermined  2022  \n",
       "4       Protest    Disruptive  External Denial of Services  2022  "
      ],
      "text/html": [
       "<div>\n",
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
       "      <th>Date</th>\n",
       "      <th>Location</th>\n",
       "      <th>Victim</th>\n",
       "      <th>Industry</th>\n",
       "      <th>Actor Location</th>\n",
       "      <th>Actor</th>\n",
       "      <th>Motive</th>\n",
       "      <th>Type</th>\n",
       "      <th>Sub-Type</th>\n",
       "      <th>Year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>31/12/2022</td>\n",
       "      <td>Iran (Islamic Republic of)</td>\n",
       "      <td>State-run Iranian Websites</td>\n",
       "      <td>Public Administration</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Protest</td>\n",
       "      <td>Disruptive</td>\n",
       "      <td>External Denial of Services</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>31/12/2022</td>\n",
       "      <td>United States of America</td>\n",
       "      <td>Housing Authority of the City of Los Angeles (...</td>\n",
       "      <td>Public Administration</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>LockBit 3.0</td>\n",
       "      <td>Financial</td>\n",
       "      <td>Exploitative</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>30/12/2022</td>\n",
       "      <td>Poland</td>\n",
       "      <td>Polish Parliament</td>\n",
       "      <td>Public Administration</td>\n",
       "      <td>Russian Federation</td>\n",
       "      <td>NoName057(16)</td>\n",
       "      <td>Protest</td>\n",
       "      <td>Disruptive</td>\n",
       "      <td>External Denial of Services</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30/12/2022</td>\n",
       "      <td>United States of America</td>\n",
       "      <td>CentraState Healthcare System</td>\n",
       "      <td>Health Care and Social Assistance</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Disruptive</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>30/12/2022</td>\n",
       "      <td>Iran (Islamic Republic of)</td>\n",
       "      <td>Iran Airlines</td>\n",
       "      <td>Transportation and Warehousing</td>\n",
       "      <td>Ukraine</td>\n",
       "      <td>rootkitsecurity</td>\n",
       "      <td>Protest</td>\n",
       "      <td>Disruptive</td>\n",
       "      <td>External Denial of Services</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 15
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-07-03T00:02:05.005925Z",
     "start_time": "2025-07-03T00:02:04.948304Z"
    }
   },
   "cell_type": "code",
   "source": [
    "year_order=df[\"Year\"].value_counts().index\n",
    "location_order=df['Location'].value_counts().index\n",
    "motive_order=df['Motive'].value_counts().index\n",
    "industry_order=df[\"Industry\"].value_counts().index"
   ],
   "id": "f6a7d898ea2c638c",
   "outputs": [],
   "execution_count": 16
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-07-03T00:02:05.927482Z",
     "start_time": "2025-07-03T00:02:05.837982Z"
    }
   },
   "cell_type": "code",
   "source": [
    "\n",
    "df.describe()"
   ],
   "id": "34539bf0ed2c3f7e",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "             Date                   Location        Victim  \\\n",
       "count        10419                     10419         10419   \n",
       "unique        2767                       155          9519   \n",
       "top     27/06/2017  United States of America  Undetermined   \n",
       "freq            78                      5110            14   \n",
       "\n",
       "                     Industry Actor Location         Actor     Motive  \\\n",
       "count                   10419          10416         10419      10419   \n",
       "unique                     21             76           956         10   \n",
       "top     Public Administration   Undetermined  Undetermined  Financial   \n",
       "freq                     2021           8269          6472       5781   \n",
       "\n",
       "              Type                            Sub-Type   Year  \n",
       "count        10419                               10415  10420  \n",
       "unique           5                                  77     11  \n",
       "top     Exploitive  Exploitation of Application Server   2022  \n",
       "freq          5397                                3616   1918  "
      ],
      "text/html": [
       "<div>\n",
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
       "      <th>Date</th>\n",
       "      <th>Location</th>\n",
       "      <th>Victim</th>\n",
       "      <th>Industry</th>\n",
       "      <th>Actor Location</th>\n",
       "      <th>Actor</th>\n",
       "      <th>Motive</th>\n",
       "      <th>Type</th>\n",
       "      <th>Sub-Type</th>\n",
       "      <th>Year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>10419</td>\n",
       "      <td>10419</td>\n",
       "      <td>10419</td>\n",
       "      <td>10419</td>\n",
       "      <td>10416</td>\n",
       "      <td>10419</td>\n",
       "      <td>10419</td>\n",
       "      <td>10419</td>\n",
       "      <td>10415</td>\n",
       "      <td>10420</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>2767</td>\n",
       "      <td>155</td>\n",
       "      <td>9519</td>\n",
       "      <td>21</td>\n",
       "      <td>76</td>\n",
       "      <td>956</td>\n",
       "      <td>10</td>\n",
       "      <td>5</td>\n",
       "      <td>77</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>27/06/2017</td>\n",
       "      <td>United States of America</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Public Administration</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Undetermined</td>\n",
       "      <td>Financial</td>\n",
       "      <td>Exploitive</td>\n",
       "      <td>Exploitation of Application Server</td>\n",
       "      <td>2022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>78</td>\n",
       "      <td>5110</td>\n",
       "      <td>14</td>\n",
       "      <td>2021</td>\n",
       "      <td>8269</td>\n",
       "      <td>6472</td>\n",
       "      <td>5781</td>\n",
       "      <td>5397</td>\n",
       "      <td>3616</td>\n",
       "      <td>1918</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "execution_count": 17
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-07-03T00:02:06.522901Z",
     "start_time": "2025-07-03T00:02:06.454025Z"
    }
   },
   "cell_type": "code",
   "source": [
    "\n",
    "df.info()"
   ],
   "id": "3b863658bdb629bb",
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10420 entries, 0 to 10419\n",
      "Data columns (total 10 columns):\n",
      " #   Column          Non-Null Count  Dtype \n",
      "---  ------          --------------  ----- \n",
      " 0   Date            10419 non-null  object\n",
      " 1   Location        10419 non-null  object\n",
      " 2   Victim          10419 non-null  object\n",
      " 3   Industry        10419 non-null  object\n",
      " 4   Actor Location  10416 non-null  object\n",
      " 5   Actor           10419 non-null  object\n",
      " 6   Motive          10419 non-null  object\n",
      " 7   Type            10419 non-null  object\n",
      " 8   Sub-Type        10415 non-null  object\n",
      " 9   Year            10420 non-null  object\n",
      "dtypes: object(10)\n",
      "memory usage: 814.2+ KB\n"
     ]
    }
   ],
   "execution_count": 18
  },
  {
   "metadata": {
    "ExecuteTime": {
     "end_time": "2025-07-03T00:02:07.712577Z",
     "start_time": "2025-07-03T00:02:06.922095Z"
    }
   },
   "cell_type": "code",
   "source": [
    "plt.figure(figsize=(20,8))\n",
    "plt.title(\"Attacck Frequency by Year\")\n",
    "sns.countplot(data=df,y=\"Year\",order=year_order)\n",
    "plt.xticks(rotation=45)"
   ],
   "id": "c17bc24780e4d95c",
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(array([   0.,  250.,  500.,  750., 1000., 1250., 1500., 1750., 2000.,\n",
       "        2250.]),\n",
       " [Text(0.0, 0, '0'),\n",
       "  Text(250.0, 0, '250'),\n",
       "  Text(500.0, 0, '500'),\n",
       "  Text(750.0, 0, '750'),\n",
       "  Text(1000.0, 0, '1000'),\n",
       "  Text(1250.0, 0, '1250'),\n",
       "  Text(1500.0, 0, '1500'),\n",
       "  Text(1750.0, 0, '1750'),\n",
       "  Text(2000.0, 0, '2000'),\n",
       "  Text(2250.0, 0, '2250')])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 2000x800 with 1 Axes>"
      ],
      "image/png": "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dvvAgQNLQJT233//+MpXvvKWbb7yyisxb968eOCBB0qAVJNh0T//+c945JFHFulrAgAAAAAAeLPu0YX16tWrrLFT09LSEpdffnlstdVWMW3atOjTp0+Hx6+00krx3HPPlf9vuOGGHe7LKd7+9re/lee+/PLLZR2g9s/v3r17LL/88m3PBwAAAAAA6CxdusLnzXKNnYcffjiOOOKIMvXaEkss0eH+vD5nzpy3PO/pp5+Oo48+OnbbbbcSBL3xxhttj5+f5wMAAAAAACxKzY0U9lx66aXl3/79+8eSSy75lnAmry+11FIdbnvyySfjS1/6Uqy11lpxyimnlNvyubXHv/n5Sy+99CJ/LQAAAAAAAA0X+IwcOTIuueSSEvYMGTKk3LbKKqvE9OnTOzwur7efpu2xxx6LL37xi7HqqquWtYBqYVBO3ZahT/vnz507N2bOnFnWDQIAAAAAAOhMXT7wGTNmTIwfPz7OOOOM2GWXXdpuHzBgQDz00ENt07OlSZMmldvTCy+8EPvtt1/07ds3Lr744lhmmWXaHtfc3BwbbbRReXzNvffeW9bxWX/99TvttQEAAAAAAKTuXfnXMHny5Bg7dmwceOCBMXDgwJg2bVrbfYMGDYrVVlutrM1zyCGHxMSJE+P++++PUaNGlftHjx4dLS0tceqpp8brr79eLqlHjx7Rs2fP2GeffeKEE04o08NlVdCJJ54Ye++9tyndAAAAAACATtelA58JEybEvHnz4rzzziuX9h599NESBh177LExdOjQUslz7rnnxuqrrx6tra1x8803l+qfnXbaqcPzRowYEYceemipFnrmmWdK6JNr9+y4445x5JFHdvIrBAAAAAAAiGhqzXSDutl/7G/inidfqPduAAAAAADUzfprrBjjDt81Zsx4LebOban37sBC09QU0bv3sjF9+ivxTmlM7bELqsuv4QMAAAAAANDVCXwAAAAAAAAqTuADAAAAAABQcQIfAAAAAACAihP4AAAAAAAAVJzABwAAAAAAoOIEPgAAAAAAABUn8AEAAAAAAKg4gQ8AAAAAAEDFCXwAAAAAAAAqTuADAAAAAABQcQIfAAAAAACAihP4AAAAAAAAVJzABwAAAAAAoOK613sHGl3f3r1i1py59d4NAAAAAIC6WafPcvXeBai8ptbW1tZ67wQAAAAAAI1t3ryWmDnz9Whp0WVN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7LAYNGhQDB48OEaNGhWzZ88u902ZMiWGDRsWm2yySey8885x2223ve02rr/++th333073PbPf/4zTj/99Nh2221jq622itGjR8fcuXM75TUBAAAAAAA0TODT2tpawp5Zs2bFuHHj4swzz4yJEyfGWWedVe4bPnx49O7dO6655prYfffdY8SIETF16tQO27jrrrvihBNOeMu2zz777Ljuuuvi1FNPjYsvvjjuvPPOOO200zrx1QEAAAAAAPyv7tGFPfHEE3HvvffG7bffXoKdlAFQVuNst912pcJn/Pjx0aNHj+jXr18JbTL8OfTQQ8tjx4wZExdccEGsvfbaHbabYVEGSMcee2x89KMfLbeddNJJ8YUvfCGOOOKI6NmzZx1eLQAAAAAA0Ki6dIXPyiuvHBdddFFb2FPz6quvxn333RcbbLBBCXtqBg4cWAKimgyKsnpnxx137PD8l156KV577bUYMGBA223rrbdemebtwQcfXKSvCQAAAAAAoKECn169epV1e2paWlri8ssvL2vuTJs2Lfr06dPh8SuttFI899xzbdevuOKKsvbPmy233HLxvve9r6wPVPPss8+Wf2fMmLGIXg0AAAAAAEADBj5vdvrpp8fDDz9cpl3LdX2WWGKJDvfn9Tlz5rzjdrp37x6f/OQn44wzzigB0SuvvFKmicvbs8oHAAAAAACgMzU3Uthz6aWXln/79+8fSy655FvCnby+1FJLzdf2jjvuuLJWT67hk+sBbbbZZqXyZ5lllllErwAAAAAAAODtdY8GMHLkyDI9W4Y9Q4YMKbetssoq8fjjj3d43PTp098yzdu/ktO/XXbZZTFz5swSHrW2tsb3v//9WGONNRbJawAAAAAAAGjYCp8xY8bE+PHjy/Rru+yyS9vtAwYMiIceeijeeOONttsmTZpUbp8fRx55ZNx2222x/PLLx9JLLx233HJLCYE++MEPLpLXAQAAAAAA0JAVPpMnT46xY8fGgQceGAMHDoxp06a13Tdo0KBYbbXV4uijj45DDjkkJk6cGPfff3+MGjVqvradQc+ZZ55ZKoJmzJhRqojy5zQ3d/kMDQAAAAAAWMx06cBnwoQJMW/evDjvvPPKpb1HH320hEHHHntsDB06NPr27RvnnnturL766vO17cMPPzxOOumk2GeffaJHjx4xbNiwcgEAAAAAAOhsTa25+Ax1s//Y38Q9T75Q790AAABYaNZfY8UYd/iuMWPGazF3bku9d4fFRFNTRO/ey8b06a+EnggakWOARqb908ia3kX7rz12QZl/DAAAAAAAoOIEPgAAAAAAABUn8AEAAAAAAKg4gQ8AAAAAAEDFCXwAAAAAAAAqTuADAAAAAABQcQIfAAAAAACAihP4AAAAAAAAVJzABwAAAAAAoOIEPgAAAAAAABUn8AEAAAAAAKg4gQ8AAAAAAEDFCXwAAAAAAAAqTuADAAAAAABQcd3rvQONrm/vXjFrztx67wYAAMBCs06f5eq9CwAA0HAEPnV2/N5b13sXAAAAFrp581qipaW13rsBAAANQ+BTZzNmvFbvXYC6WWGFno4BGpb2TyPT/ml0jXIMZNgj8AEAgM4j8KmzlpYc9VbvvYDO19T0fyM/W/UD0GC0fxqZ9k+jcwwAAACLSvMi2zIAAAAAAACdQuADAAAAAABQcQIfAAAAAACAihP4AAAAAAAAVJzABwAAAAAAoOIEPgAAAAAAABUn8AEAAAAAAKg4gQ8AAAAAAEDFda/3DjS65ubmaBa70cC6dXMA0Li0fxqZ9r9wtLS0lgsAAAAIfOpshRV61nsXoK4cAzQy7Z9Gpv0vHPPmtcTMma8LfQAAABD41NvIK++IR6a+VO/dAACgYtbps1ycss/gaG5uEvgAAAAg8Km3p6a/HI88I/ABAAAAAAAWnMnTAQAAAAAAKk7gAwAAAAAAUHECHwAAAAAAgIoT+AAAAAAAAFScwAcAAAAAAKDiBD4AAAAAAACNFvg8/fTTi2ZPAAAAAAAA6JzA5/Of/3w8+OCDC/bTAAAAAAAAqH/g07t373jxxRcX/p4AAAAAAACwQLq/2ydssMEGccghh8RGG20Ua6yxRiyxxBId7h81atSC7QkAAAAAAACdE/ikT3/60wv20wAAAAAAAKh/4KOCBwAAAAAAoOKBT2tra0yYMCEee+yxmDdvXtvtc+bMiYcffjguuuiihb2PAAAAAAAALMzAZ+TIkXH11VeXtXzuv//+2HTTTePpp5+O6dOnx+c///l3uzkAAAAAAADeo+Z3+4Rf//rX8b3vfS/Gjx8f73//++PEE0+MiRMnxi677BL//Oc/Y3Hz/PPPx2GHHRaDBg2KwYMHlynpZs+eXe6bMmVKDBs2LDbZZJPYeeed47bbbnvbbVx//fWx7777drjtH//4R6y33nodLltuuWWnvCYAAAAAAID3VOHz6quvxoc//OHy//79+5cqn3XXXTcOOuig+OpXvxqLk5x+LsOeXr16xbhx40pIc8wxx0Rzc3McddRRMXz48PIarrnmmrj55ptjxIgRJdBaffXV27Zx1113xQknnBAbbbRRh20//vjjsfzyy8cNN9zQdltuFwAAAAAAYLEPfNZaa62yVk+GIhn0ZODz2c9+toQrr7zySixOnnjiibj33nvj9ttvj969e5fbMgAaPXp0bLfddqXCJyuVevToEf369Ys777yzhD+HHnpoeeyYMWPiggsuiLXXXvttt73OOuvEyiuv3OmvCwAAAAAA4D0FPvvtt18ceeSRceqpp5Zp0IYOHRrdu3ePe+65JwYOHBiLkwxjLrroorawp32V0n333VfWIcqwpyb3PwOimgyKLr744vjjH/8Yf/rTn95S4fN2QRAAAAAAAMBiH/jstddeJeioVcVkFcxVV11VpnmrVcYsLnIqt1y3p6alpSUuv/zy2GqrrWLatGnRp0+fDo9faaWV4rnnnmu7fsUVV5R/M/B5s8mTJ8fcuXNjzz33LOsEbb755nH00Ue/ZZsAAAAAAACLXeCTtthii/JvromzzTbbxLbbbhtNTU2xuDv99NPLdHRXX311/PjHP44llliiw/15fc6cOfO1rZzSbcUVVywhT05nd+aZZ8bBBx9cwq9u3botolcAAAAAAACwEAKfDDfOP//8Epjkmj033XRT/OAHPygVP8cdd9xbQpTFKey59NJLSzDTv3//WHLJJWPmzJkdHpNhz1JLLTVf2/vVr35VQq7a488+++wSfOVUcZttttkieQ0AAAAAAABvpznepXPPPTeuv/76OO2009rCnc985jNlvZvvfve7sTgaOXJkXHLJJSX0GTJkSLltlVVWienTp3d4XF6f3ynZll566Q7hUE4Ht/zyy5fp3QAAAAAAABbrwOfnP/95nHzyyfHxj3+8bRq3nNZt9OjRceONN8biJtcYGj9+fJxxxhmxyy67tN0+YMCAeOihh+KNN95ou23SpEnl9nfy6quvlmnt7rrrrrbbMuiZMWNGfOADH1gErwIAAAAAAGAhBj4vvvji21bB9OrVK15//fVYnEyePDnGjh0bBxxwQAwcODCmTZvWdhk0aFCsttpqZQ2exx57LC688MK4//77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lClTYtiwYbHJJpvEzjvvHLfddtvbbuP666+Pfffdt+363//+91hvvfXe9vLnP/+5014bAAAAAABA6t6Vfw2tra0l7OnVq1eMGzcu/vGPf8QxxxwTzc3NcdRRR8Xw4cOjf//+cc0118TNN98cI0aMiF//+tex+uqrt23jrrvuihNOOCE22mijtttWW221t4RDp512Wjz11FMlPAIAAAAAAOhMXTrweeKJJ+Lee++N22+/PXr37l1uywBo9OjRsd1225UKn/Hjx0ePHj2iX79+ceedd5bw59BDDy2PHTNmTFxwwQWx9tprd9hut27dYuWVV267fvfdd8dNN90Uv/jFL+J973tfJ79KAAAAAACg0XXpKd0ylLnooovawp6aV199Ne67777YYIMNSthTM3DgwBIQ1WRQdPHFF8eOO+74b3/O97///dh7771LaAQAAAAAANDZunTgk1O55bo9NS0tLXH55ZfHVlttFdOmTYs+ffp0ePxKK60Uzz33XNv1K664oqz98+9MmjSphEQHHXTQIngFAAAAAAAADR74vNnpp58eDz/8cBxxxBExa9asWGKJJTrcn9fnzJnzrrZ55ZVXxic/+clYZZVVFvLeAgAAAAAAzJ/mRgp7Lr300vJv//79Y8kll3xLuJPXl1pqqfne5ty5c2PChAnx6U9/ehHsMQAAAAAAwPxpiMBn5MiRcckll5SwZ8iQIeW2rMiZPn16h8fl9TdP8/bv5FRuGfpss802C32fAQAAAAAA5leXD3zGjBkT48ePjzPOOCN22WWXttsHDBgQDz30ULzxxhsd1uPJ2+fXfffdFxtuuGGpFgIAAAAAAKiXLh34TJ48OcaOHRsHHHBADBw4MKZNm9Z2GTRoUKy22mpx9NFHx2OPPRYXXnhh3H///bHnnnvO9/bzef369VukrwEAAAAAAOCddI8uLNfXmTdvXpx33nnl0t6jjz5awqBjjz02hg4dGn379o1zzz03Vl999fnefk4B96EPfWgR7DkAAAAAAMD8a2ptbW19F49nIdt/7G/inidfqPduAADwLqy/xoox7vBdY8aM12Lu3JZ67w4V0tQU0bv3sjF9+ivhTIxGo/3T6BwDNDLtn0bW9C7af+2xC6pLT+kGAAAAAADQCAQ+AAAAAAAAFSfwAQAAAAAAqDiBDwAAAAAAQMUJfAAAAAAAACpO4AMAAAAA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E/gAAAAAAABUnMAHAAAAAACg4gQ+AAAAAAAAFSfwAQAAAAAAqDiBDwAAAAAAQMU1TOAzZ86c2HXXXeOPf/xj220PPvhgfO5zn4tNN9009t5777j33ns7POeOO+4ozxkwYEB86UtfiilTpnS4/8c//nEMHjy4PP+YY46JWbNmddrrAQAAAAAAaKjAZ/bs2fH1r389HnvssbbbXnzxxRg2bFj0798/rr766th5553jK1/5SkydOrXcn/8OHz48hg4dWu5fccUV45BDDonW1tZy/0033RRjxoyJk08+OS699NK477774vTTT6/bawQAAAAAABpXlw98Hn/88VK98/TTT3e4/brrrovll18+TjzxxOjXr18JfwYOHBhXXHFFuf+qq66KD3/4w7HffvvFuuuuG6NGjYpnnnkm/vSnP5X7L7vssvjyl78cH//4x2PjjTeOk046Ka655hpVPgAAAAAAQKfr8oFPBjRbbrll/OxnP+twe07PtuGGG0a3bt3abltvvfXapnXLip3NN9+87b6ll166PD7vnzdvXjzwwAMd7t9kk03in//8ZzzyyCOd8roAAAAAAABqukcXt88++7zt7b17935LOPPcc8/FjBkzyv+nTZsWffr06XD/SiutVB7z8ssvl2ni2t/fvXv3UjGU9wMAAAAAAHSmLl/h86/suOOOcf/998eVV14Zc+fOjT/84Q8xYcKEUqWTcmq2JZZYosNz8vqcOXPijTfeaLv+dvcDAAAAAAB0poYNfPr37x8jR44sa/NstNFGceaZZ8bnP//56NmzZ7l/ySWXfEt4k9dzare8r3b97e4HAAAAAADoTA0b+KTPfvaz8Ze//CVuueWWuPbaa6OpqSnWXHPNct8qq6wS06dP7/D4vL7yyiuXqdsy9Gl/f1YJzZw5s9wPAAAAAADQmRo28LnrrrviiCOOiG7dupW1eFpbW8u0bltuuWW5f8CAATFp0qS2x+cUbw8//HC5vbm5uVQFtb//3nvvLev4rL/++nV5PQAAAAAAQONq2MBnnXXWiYkTJ8ZPf/rTmDJlSpx00knxj3/8I/bYY4+26p+77747Lrzwwnjsscfi6KOPLtU/tUBon332iYsvvjhuvvnmshbQiSeeGHvvvbcp3QAAAAAAgE7XsIFPTtl21llnxU9+8pPYbbfd4sknn4xLLrmkbQ2fDHfOOeecuOaaa2LPPfcs07Wde+65Zdq3tMsuu8RBBx0UJ5xwQuy3336x8cYbx5FHHlnnVwUAAAAAADSiptacy4y6mjHjtZg7t6XeuwGdKrPT3r2XjenTXwnvQjQa7Z9Gpv3T6BwDNDLtn0bnGKCRaf80sqZ30f5rj11QDVvhAwAAAAAA0FUIfAAAAAAAACpO4AMAAAAAAFBxAh8AAAAAAICKE/gAAAAAAABUnMAHAAAAAACg4gQ+AAAAAAAAFSfwAQAAAAAAqDiBDwAAAAAAQMUJfAAAAAAAACpO4AMAAAAAAFBxAh8AAAAAAICKE/gAAAAAAABUnMAHAAAAAACg4gQ+AAAAAAAAFSfwqbN581qipaW13rsBAAAAAABUmMCnzv7xj9cFPgAAAAAAwHsi8Kmz1lZhDwAAAAAA8N4IfAAAAAAAACpO4AMAAAAAAFBx3eu9A42uqel/L9Boau1e+6cRaf80Mu2fRucYoJFp/zQ6xwCNTPunkTW9i/b/Xo+RplaLyAAAAAAAAFSaKd0AAAAAAAAqTuADAAAAAABQcQIfAAAAAACAihP4AAAAAAAAVJzABwAAAAAAoOIEPgAAAAAAABUn8AEAAAAAAKg4gQ8AAAAAAEDFCXwAAAAAAAAqTuADAAAAAABQcd3rvQON5Pnnn4/3ve99sdRSS0WPHj3qvTuwWGltbY2mpqZ67wbUhfYPAAAA0Fh9QWlh9wcJfDrJGWecEbfddlu88MILscUWW8TgwYNj6NCh9d4tqKu//vWvscQSS5Qg9P3vf3+9dwc6lfZPo3vyySfLAJj8ctunT5967w4sFqG/AQA0Iu2eRqb9AzS2pkXwGSDw6QTXXXddXHvttfHd7343pk2bFs8++2ycfPLJ8dRTT8URRxxR792Dusjj4Ve/+lUsvfTSMX369DjwwAPjU5/6VKy11lr13jVY5LR/Gt33vve9+N3vftd2/eCDD45ddtmlhKDQaJ555pno2bNnNDc3x3LLLafzj4bz4osvRq9evWLevHnlu1FLS0s5HqARaP80uldffbUMAsvvP926dXMM0DAuueSSuOeee8og4A996EOx//77L7RtC3w6QQY8G2+8cWy99dbl+j//+c/o169f/Nd//Ve88cYbcfTRR9d7F6FT3XnnnXH99dfHD37wgzKqOysdRo8eXUZ777nnnjFw4MB67yIsMto/je7mm2+On//853HWWWeVE7vHH388jj/++Hj00UfjC1/4guCThpsFII+JDHi6d+8eX//612ObbbYp/4dGkN+H/vCHP5Rz5NVXXz2+9rWvlXNnaATaP43u3HPPjbvvvruEPptttlk5H87+UoNf6OouvPDCuPjii2OfffaJ2bNnxw9/+MPSV3TkkUfGeuut957bv8i0E+bhy6Tutddea7s9E+tPfvKT5Y3tiiuuKP9CI8lKt+zozo7t7Njbcccd4/TTTy9Vb3lM3H///fXeRVhksqJH+6eRTZ06tZzI5RS3gwYNKl9yzzvvvLjxxhvjxz/+cTz33HP13kXoFL/+9a/jqquuimOPPTaOOuqo+MQnPhHDhw8vJ4C59id0ddn+x48fX6o8P//5z8dqq61WPhOuueaamDt3br13DxYp7Z9G95Of/KRcdtttt9hqq63KefJ//Md/lE5vYQ9d2RtvvFH6fbIQ5D//8z/LeUCeC2fF56hRo0oIWssUFpTAZxGqvUF97GMfiz//+c8xbty4cj1LE7NEcdttt43TTjstLrvssvjNb35T572FRS9HbaS11167JNj33ntv2305muNb3/pW/P3vf4+rr766vNFBV1L7wO7bt2/5gNf+aTRz5swp/2aHRh4D2d5TfifKtQ3zO9FNN93U9n3pvX7JhcXdlClTYpNNNikVPR/96Efj0EMPjVNOOaWE/z/96U99FtDlTZ48OT7+8Y+XsDM7+U444YRS5XbccceV4wC6Mu2fRvfwww/HZz7zmdhjjz3Kchc5AOazn/1sHHDAATFhwoS28wToapZaaqlyPvzII4+0nfeuuOKKJQDNis9zzjmnzADzXgh8OsEHP/jB8saV5bo33HBDh9AnP+Azza51/OncoKvK9p9rWWW7X3nllWOllVYqHXszZsxoe0yWr2fC/dvf/lYISpcdBLDKKquU9p9tXPunUWQ186233toWembbz1FMtWMjv/985CMfiVNPPbWUs+dxYGQfXVXt+35We+ax8MILL7Tdl50eOQAgw/+c+jDp7KCryjWrZs6c2TYgIO23335lms/vfOc7Zb3D5BigK6m152z/+Rmg/dOocu3O2mxI+d1o+eWXL9+BvvrVr5aqh0mTJrX1nUJXMm/evBgwYEA8/fTTpao/z3uzsnPZZZeNCy64oFS75brP74XAp5NkSv3FL36xTNvzy1/+styWb1y5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1qxZ9d416BS+B9Holl9++ejZs2dp+1nZk4FPrmFVD6Z0AwAAWEhqp1c50u/VV1+NZZZZpt67BJ3KMUAj0/5pdI4BGtV9990Xn/vc5+J973tfCfw32GCDuu2LwAcAAGARTO1Q+xcajWOARqb90+gcAzSiWbNmxfe///3YZ5996r5mocAHAAAAAABgAc2dOze6d+8e9SbwAQAAAAAAqDgrJwIAAAAAAFScwAcAAAAAAKDiBD4AAAAAAAAVJ/ABAAAAAACoOIEPAAAAAABAxQl8AAAAAAAAKk7gAwAAUFFTpkyJW265pd67AQAALAYEPgAAABV1zDHHxP3331/v3QAAABYDAh8AAAAAAICKE/gAAAAsBE899VR89atfjU033TQ+9rGPxWWXXVZunzx5crl9s802i8GDB8eYMWOipaWl3HfOOefEvvvu22E722+/fVx77bXl/3nfeeedV56/8cYbx5AhQ+IPf/hDue9b3/pW/OlPfyrbe/M2AACAxiPwAQAAeI9mz54d++23X/Ts2TOuvPLKOOGEE+LMM8+MX/ziF7HPPvtEnz594qqrropvf/vbcfnll7eFQfPj/PPPj1122SVuuOGGWH/99eP4448vgdGxxx5bwqX8uRkcAQAAja17vXcAAACg6m677bZ46aWX4jvf+U4ss8wyse6668Zxxx0XM2fOjKWXXjpGjhwZ3bt3j379+sW0adPi3HPPjWHDhs3Xtj/60Y/G0KFDy/+/9rWvxe677162scoqq8T73ve+6NGjRyy//PKL+BUCAACLOxU+AAAA79GTTz4Z66yzTgl7aj772c/GE088ERtuuGEJe2qyKicDm5dffnm+tr322mu3/b+2/blz5y7U/QcAAKpP4AMAAPAetQ902ltyySXfcltt/Z558+ZFU1PTW+5/c5iTVTxv1tra+h72FgAA6IpM6QYAAPAeZRXOU089FbNmzSpTuKXRo0fHT3/60+jdu3f885//bAtu7rnnnlhxxRXLNGx522uvvda2nfx/Tg0HAADwbqnwAQAAeI+23XbbEuyccMIJMXny5JgwYUKMHz8+zjrrrJgzZ07b7TfffHOcc8458fnPf75U92y00UbxyCOPxI033limhcvHNTfP/2lart/zt7/9LV588cVF+voAAIDFnwofAACAhTCl29ixY/9fO3dsAiEQBFB0rg07MbcADYxdQbADA0Nh67Evm/DA4OJLDm7gvXwZNv7MxHEcMQzDE3+2bYuu66Jpmqi1Rt/3z2bPNE2xruvzrm3bKKV8Qs88z3Fd19dzx3GMfd9jWZY4z/OHPwQAAP7d63b8GQAAAAAAIDUn3QAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAAJITfAAAAAAAACK3N61xCBJzv7QCAAAAAElFTkSuQmCC"
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "execution_count": 19
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
