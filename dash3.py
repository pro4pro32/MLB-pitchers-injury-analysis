import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import numpy as np

# ================== WYBÓR JĘZYKA ==================
language = st.sidebar.selectbox(
    "Choose language / Wybierz język / Idioma / Langue / 言語",
    ["English", "Polski", "Español", "Français", "日本語"],
    index=0
)

translations = {
    "English": {
        "title": "🏥 MLB Injury Dashboard • % on IL",
        "main_team": "Main Team",
        "compare_team": "Compare With",
        "role_filter": "Role Filter",
        "min_days": "Min. Active Days",
        "all": "All",
        "starters": "Starters",
        "relievers": "Relievers",
        "percent_il": "% Time on IL",
        "additional_scatter": "Additional Scatter Plots",
        "select_scatter": "Select Scatter Type",
        "compare_team_placeholder": "choose second team",
        "file_missing": "Missing file for",
        "grouping": "Grouping on chart",
        "starters_first": "Starters on top",
        "relievers_first": "Relievers on top",
        "no_grouping": "Mixed (no grouping)",
        "sort_direction": "Sort direction within group",
        "descending": "Descending (% IL high to low)",
        "ascending": "Ascending (% IL low to high)",
        "league_wide": "🏟️ All MLB Pitchers",
        "league_chart": "All MLB Pitchers Chart • % on IL",
        "league_table": "All MLB Pitchers Table",
        "show_additional_scatter": "Show additional scatter plots",
        "show_league_wide_option": "Show all MLB Pitchers statistics",
        "league_additional_scatter": "Additional Scatter Plots - All MLB Pitchers"
    },
    "Polski": {
        "title": "🏥 MLB Injury Dashboard • % na IL",
        "main_team": "Drużyna główna",
        "compare_team": "Porównaj z drużyną",
        "role_filter": "Filtr roli",
        "min_days": "Min. aktywne dni",
        "all": "Wszystko",
        "starters": "Starterzy",
        "relievers": "Relieverzy",
        "percent_il": "Procent czasu na IL",
        "additional_scatter": "Dodatkowe wykresy zależności",
        "select_scatter": "Wybierz typ scattera",
        "compare_team_placeholder": "wybierz drugą drużynę",
        "file_missing": "Brak pliku dla",
        "grouping": "Grupowanie na wykresie",
        "starters_first": "Starterzy na górze",
        "relievers_first": "Relieverzy na górze",
        "no_grouping": "Mieszanka (bez grupowania)",
        "sort_direction": "Kierunek sortowania w grupie",
        "descending": "Malejąco (% IL od największego)",
        "ascending": "Rosnąco (% IL od najmniejszego)",
        "league_wide": "🏟️ Wszyscy miotacze MLB",
        "league_chart": "Wykres wszystkich miotaczy MLB • % na IL",
        "league_table": "Tabela wszystkich miotaczy MLB",
        "show_additional_scatter": "Pokaż dodatkowe wykresy punktowe",
        "show_league_wide_option": "Pokaż statystyki wszystkich miotaczy MLB",
        "league_additional_scatter": "Dodatkowe wykresy punktowe – wszyscy miotacze MLB"
    },
    "Español": {
        "title": "🏥 Panel de Lesiones MLB • % en IL",
        "main_team": "Equipo Principal",
        "compare_team": "Comparar con",
        "role_filter": "Filtro de Rol",
        "min_days": "Días activos mínimos",
        "all": "Todos",
        "starters": "Titulares",
        "relievers": "Relevistas",
        "percent_il": "% de tiempo en IL",
        "additional_scatter": "Gráficos de dispersión adicionales",
        "select_scatter": "Seleccionar tipo de scatter",
        "compare_team_placeholder": "elige segundo equipo",
        "file_missing": "Archivo faltante para",
        "grouping": "Agrupación en el gráfico",
        "starters_first": "Titulares arriba",
        "relievers_first": "Relevistas arriba",
        "no_grouping": "Mezclado (sin agrupar)",
        "sort_direction": "Dirección de ordenamiento",
        "descending": "Descendente (% IL alto a bajo)",
        "ascending": "Ascendente (% IL bajo a alto)",
        "league_wide": "🏟️ Todos los Lanzadores de MLB",
        "league_chart": "Gráfico de todos los lanzadores MLB • % en IL",
        "league_table": "Tabla de todos los lanzadores MLB",
        "show_additional_scatter": "Mostrar gráficos de dispersión adicionales",
        "show_league_wide_option": "Mostrar estadísticas de todos los lanzadores MLB",
        "league_additional_scatter": "Gráficos de dispersión adicionales - Todos los lanzadores MLB"
    },
    "Français": {
        "title": "🏥 Tableau de Bord des Blessures MLB • % sur IL",
        "main_team": "Équipe Principale",
        "compare_team": "Comparer avec",
        "role_filter": "Filtre de Rôle",
        "min_days": "Jours actifs minimum",
        "all": "Tous",
        "starters": "Starters",
        "relievers": "Relievers",
        "percent_il": "% de temps sur IL",
        "additional_scatter": "Graphiques de dispersion supplémentaires",
        "select_scatter": "Sélectionner le type de scatter",
        "compare_team_placeholder": "choisir une deuxième équipe",
        "file_missing": "Fichier manquant pour",
        "grouping": "Groupement sur le graphique",
        "starters_first": "Starters en haut",
        "relievers_first": "Relievers en haut",
        "no_grouping": "Mixte (sans regroupement)",
        "sort_direction": "Direction de tri",
        "descending": "Descendant (% IL élevé à faible)",
        "ascending": "Ascendant (% IL faible à élevé)",
        "league_wide": "🏟️ Tous les Lanceurs MLB",
        "league_chart": "Graphique de tous les lanceurs MLB • % sur IL",
        "league_table": "Tableau de tous les lanceurs MLB",
        "show_additional_scatter": "Afficher les graphiques de dispersion supplémentaires",
        "show_league_wide_option": "Afficher les statistiques de tous les lanceurs MLB",
        "league_additional_scatter": "Graphiques de dispersion supplémentaires - Tous les lanceurs MLB"
    },
    "日本語": {
        "title": "🏥 MLB 故障者ダッシュボード • IL在籍率%",
        "main_team": "メイン球団",
        "compare_team": "比較する球団",
        "role_filter": "役割フィルター",
        "min_days": "最小活動日数",
        "all": "すべて",
        "starters": "先発",
        "relievers": "リリーフ",
        "percent_il": "IL在籍率 (%)",
        "additional_scatter": "追加の散布図",
        "select_scatter": "散布図の種類を選択",
        "compare_team_placeholder": "2番目のチームを選択",
        "file_missing": "ファイルが見つかりません：",
        "grouping": "グラフのグループ化",
        "starters_first": "先発を上部に",
        "relievers_first": "リリーフを上部に",
        "no_grouping": "混合（グループ化なし）",
        "sort_direction": "グループ内の並び順",
        "descending": "降順（IL% 高い順）",
        "ascending": "昇順（IL% 低い順）",
        "league_wide": "🏟️ MLB 全投手",
        "league_chart": "MLB 全投手チャート • IL在籍率",
        "league_table": "MLB 全投手テーブル",
        "show_additional_scatter": "追加の散布図を表示",
        "show_league_wide_option": "MLB 全投手の統計を表示",
        "league_additional_scatter": "追加の散布図 - MLB 全投手"
    }
}

t = translations[language]

# ================== SCATTER OPTIONS (bez "(symulacja)") ==================
scatter_options = [
    "FB Spin vs % IL", 
    "FB Velo vs % IL",
    "Breaking % vs % IL", 
    "Offspeed Spin vs % IL"   # <-- usunięto "(symulacja)"
]

x_map = {
    "FB Spin vs % IL": "fb_spin",
    "FB Velo vs % IL": "fb_velo",
    "Breaking % vs % IL": "breaking_%",
    "Offspeed Spin vs % IL": "fb_spin"   # <-- zaktualizowano klucz
}

# ================== FUNKCJE POMOCNICZE ==================
def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    rename_dict = {
        'il_days': 'il_days_apr_sep',
        'active_days': 'active_days_apr_sep',
        'pct_injured_%': 'pct_injured_apr_sep_%',
        'g2025': 'games_2025',
        'ip2025': 'innings_2025'
    }
    df = df.rename(columns=rename_dict)
   
    if 'innings_2025' in df.columns and 'games_2025' in df.columns:
        df['IP_per_game'] = df['innings_2025'] / df['games_2025'].replace(0, np.nan)
    else:
        df['IP_per_game'] = 0.0
   
    df['IP_per_game'] = df['IP_per_game'].fillna(0).round(2)
    df['Role'] = df['IP_per_game'].apply(lambda x: "Starter" if x >= 3.5 else "Reliever")
   
    forced_starters = ["Gerrit Cole", "Tatsuya Imai", "Cody Ponce"]
    df.loc[df['player'].isin(forced_starters), 'Role'] = "Starter"
   
    return df

def sort_dataframe(df: pd.DataFrame, grouping: str, ascending_pct: bool):
    if grouping == t["no_grouping"]:
        df_sorted = df.sort_values('pct_injured_apr_sep_%', ascending=ascending_pct)
        ordered = df_sorted['player'].tolist()
    elif grouping == t["starters_first"]:
        starter_df = df[df['Role'] == 'Starter'].sort_values('pct_injured_apr_sep_%', ascending=ascending_pct)
        reliever_df = df[df['Role'] == 'Reliever'].sort_values('pct_injured_apr_sep_%', ascending=ascending_pct)
        df_sorted = pd.concat([reliever_df, starter_df])
        ordered = df_sorted['player'].tolist()
    elif grouping == t["relievers_first"]:
        reliever_df = df[df['Role'] == 'Reliever'].sort_values('pct_injured_apr_sep_%', ascending=ascending_pct)
        starter_df = df[df['Role'] == 'Starter'].sort_values('pct_injured_apr_sep_%', ascending=ascending_pct)
        df_sorted = pd.concat([starter_df, reliever_df])
        ordered = df_sorted['player'].tolist()
    else:
        df_sorted = df
        ordered = df['player'].tolist()
    return df_sorted, ordered

def load_league_data(mlb_teams: list) -> pd.DataFrame:
    all_dfs = []
    for team in mlb_teams:
        file_name = f"{team.replace(' ', '_')}_injury_analysis_MLB_only.csv"
        if Path(file_name).exists():
            try:
                df = pd.read_csv(file_name)
                df = prepare_dataframe(df)
                df['Team'] = team
                all_dfs.append(df)
            except Exception:
                pass
    return pd.concat(all_dfs, ignore_index=True) if all_dfs else pd.DataFrame()

# ================== KONFIGURACJA DASHBOARDU ==================
st.set_page_config(page_title=t["title"], layout="wide", page_icon="🏥")
st.title(t["title"])

mlb_teams = [
    "Arizona Diamondbacks", "Atlanta Braves", "Baltimore Orioles", "Boston Red Sox",
    "Chicago White Sox", "Chicago Cubs", "Cincinnati Reds", "Cleveland Guardians",
    "Colorado Rockies", "Detroit Tigers", "Houston Astros", "Kansas City Royals",
    "Los Angeles Angels", "Los Angeles Dodgers", "Miami Marlins", "Milwaukee Brewers",
    "Minnesota Twins", "New York Yankees", "New York Mets", "Athletics",
    "Philadelphia Phillies", "Pittsburgh Pirates", "San Diego Padres", "San Francisco Giants",
    "Seattle Mariners", "St. Louis Cardinals", "Tampa Bay Rays", "Texas Rangers",
    "Toronto Blue Jays", "Washington Nationals"
]

# ================== FILTRY ==================
team1 = st.sidebar.selectbox(t["main_team"], mlb_teams)

# Opcja "brak porównania" przetłumaczona dla każdego języka
no_comparison = {
    "English": "--- no comparison ---",
    "Polski": "--- brak porównania ---",
    "Español": "--- sin comparación ---",
    "Français": "--- pas de comparaison ---",
    "日本語": "--- 比較なし ---"
}[language]

team2_options = [no_comparison] + [t for t in mlb_teams if t != team1]
team2 = st.sidebar.selectbox(t["compare_team"], team2_options)

role_filter = st.sidebar.radio(t["role_filter"], [t["all"], t["starters"], t["relievers"]])
min_days = st.sidebar.slider(t["min_days"], 30, 2000, 50, step=20)

col_filters = st.columns([1, 1])
with col_filters[0]:
    grouping = st.radio(t["grouping"], [t["starters_first"], t["relievers_first"], t["no_grouping"]], horizontal=True)
with col_filters[1]:
    sort_dir = st.radio(t["sort_direction"], [t["ascending"], t["descending"]], horizontal=True)

ascending_pct = (sort_dir == t["ascending"])

# ================== DANE DRUŻYNY GŁÓWNEJ ==================
file_path = f"{team1.replace(' ', '_')}_injury_analysis_MLB_only.csv"
if not Path(file_path).exists():
    st.error(f"{t['file_missing']} {team1}")
    st.stop()

df1 = pd.read_csv(file_path)
df1 = prepare_dataframe(df1)
df1 = df1[df1['active_days_apr_sep'] >= min_days]

if role_filter == t["starters"]:
    df1 = df1[df1['Role'] == "Starter"]
elif role_filter == t["relievers"]:
    df1 = df1[df1['Role'] == "Reliever"]

df1, ordered_players = sort_dataframe(df1, grouping, ascending_pct)

# ================== GŁÓWNY WYKRES ==================
st.subheader(f"{team1} – {t['percent_il']}")
fig_bar = px.bar(
    df1, x='pct_injured_apr_sep_%', y='player', orientation='h',
    color='Role', color_discrete_map={"Starter": "#d62728", "Reliever": "#1f77b4"}
)
fig_bar.update_traces(width=0.35)
for val in range(10, 101, 10):
    fig_bar.add_vline(x=val, line=dict(color="gray", width=0.5, dash="dash"))
fig_bar.update_layout(
    height=700, bargap=0.25, xaxis_range=[0, 100],
    yaxis={'tickfont': {'size': 15}, 'categoryorder': 'array', 'categoryarray': ordered_players}
)
st.plotly_chart(fig_bar, use_container_width=True)

# ================== TABELA ==================
st.subheader("Details – " + team1 if language == "English" else 
             "Szczegóły – " + team1 if language == "Polski" else
             "Detalles – " + team1 if language == "Español" else
             "Détails – " + team1 if language == "Français" else
             "詳細 – " + team1)

st.dataframe(
    df1[['player', 'Role', 'IP_per_game', 'il_days_apr_sep', 'active_days_apr_sep',
         'pct_injured_apr_sep_%', 'fb_velo', 'fb_spin', 'breaking_%']].round(2),
    use_container_width=True, height=380
)

# ================== DODATKOWE SCATTERY ==================
show_scatter = st.checkbox(t["show_additional_scatter"], value=True, key="show_scatter_main")
if show_scatter:
    st.subheader(t["additional_scatter"])
    scatter_choice = st.selectbox(t["select_scatter"], scatter_options, key="scatter_main")
   
    fig_scatter = px.scatter(
        df1, x=x_map[scatter_choice], y='pct_injured_apr_sep_%',
        size='active_days_apr_sep', color='Role', hover_name='player', title=scatter_choice
    )
    fig_scatter.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig_scatter, use_container_width=True)

# ================== PORÓWNANIE Z DRUGĄ DRUŻYNĄ ==================
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"1. {team1}")
    st.plotly_chart(fig_bar, use_container_width=True, key="compare1")

with col2:
    display_team2 = team2 if team2 != no_comparison else t["compare_team_placeholder"]
    st.subheader(f"2. {display_team2}")
    
    if team2 != no_comparison:
        file2 = f"{team2.replace(' ', '_')}_injury_analysis_MLB_only.csv"
        if Path(file2).exists():
            df2 = pd.read_csv(file2)
            df2 = prepare_dataframe(df2)
            df2 = df2[df2['active_days_apr_sep'] >= min_days]
           
            if role_filter == t["starters"]:
                df2 = df2[df2['Role'] == "Starter"]
            elif role_filter == t["relievers"]:
                df2 = df2[df2['Role'] == "Reliever"]
           
            df2, ordered2 = sort_dataframe(df2, grouping, ascending_pct)
           
            fig2 = px.bar(
                df2, x='pct_injured_apr_sep_%', y='player', orientation='h',
                color='Role', color_discrete_map={"Starter": "#d62728", "Reliever": "#1f77b4"}
            )
            fig2.update_traces(width=0.35)
            for val in range(10, 101, 10):
                fig2.add_vline(x=val, line=dict(color="gray", width=0.5, dash="dash"))
            fig2.update_layout(height=700, bargap=0.25, xaxis_range=[0, 100],
                               yaxis={'tickfont': {'size': 15}, 'categoryorder': 'array', 'categoryarray': ordered2})
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info(f"{t['file_missing']} {team2}")
    else:
        st.info(t['compare_team_placeholder'])

# ================== SEKCJA LEAGUE-WIDE ==================
st.divider()
show_league_wide = st.checkbox(t["show_league_wide_option"], value=True, key="league_checkbox")

if show_league_wide:
    st.header(t["league_wide"])
    league_df_raw = load_league_data(mlb_teams)
    if not league_df_raw.empty:
        league_df = league_df_raw[league_df_raw['active_days_apr_sep'] >= min_days].copy()
       
        if role_filter == t["starters"]:
            league_df = league_df[league_df['Role'] == "Starter"]
        elif role_filter == t["relievers"]:
            league_df = league_df[league_df['Role'] == "Reliever"]
       
        league_df, ordered_league = sort_dataframe(league_df, grouping, ascending_pct)
       
        st.subheader(t["league_chart"])
        num_players = len(league_df)
        fig_league = px.bar(league_df, x='pct_injured_apr_sep_%', y='player', orientation='h',
                            color='Role', color_discrete_map={"Starter": "#d62728", "Reliever": "#1f77b4"})
        fig_league.update_layout(height=max(900, num_players * 18), xaxis_range=[0, 100])
        st.plotly_chart(fig_league, use_container_width=True)

        st.subheader(t["league_table"])
        st.dataframe(
            league_df[['player', 'Team', 'Role', 'IP_per_game', 'il_days_apr_sep',
                       'active_days_apr_sep', 'pct_injured_apr_sep_%',
                       'fb_velo', 'fb_spin', 'breaking_%']].round(2),
            use_container_width=True, height=650
        )

        st.subheader(t["league_additional_scatter"])
        scatter_league = st.selectbox(t["select_scatter"], scatter_options, key="league_scatter")
        fig_l = px.scatter(league_df, x=x_map[scatter_league], y='pct_injured_apr_sep_%',
                           size='active_days_apr_sep', color='Role', hover_name='player')
        fig_l.update_layout(yaxis_range=[0, 100])
        st.plotly_chart(fig_l, use_container_width=True)