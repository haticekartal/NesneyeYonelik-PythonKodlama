"""
Ders dokümanındaki kavramsal şekilleri üreten kod (EK)

PDF'de kodu gösterilmeyen şekiller: yapay zekâ / makine öğrenmesi / derin öğrenme
ilişkisi, iş akışı, öğrenme türleri, sınıflandırma-regresyon, eğitim-tahmin
aşamaları, train-test split, underfitting/overfitting, Iris çiçeği anatomisi ve
üç türün ölçekli şeması.

Çalıştırma: python ek_kavramsal_sekiller.py
Şekiller "sekiller" klasörüne PNG olarak kaydedilir.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch, FancyArrowPatch
from sklearn.datasets import load_iris

plt.rcParams.update({"font.family": ["Inter", "DejaVu Sans"], "font.size": 10, "axes.edgecolor": "#9aa6b2",
                     "axes.labelcolor": "#33404d", "xtick.color": "#52514e", "ytick.color": "#52514e",
                     "axes.spines.top": False, "axes.spines.right": False})
NAVY, TEXT, MUTED = "#1f4e79", "#10263d", "#5b6b7c"
C = {"setosa": "#2a78d6", "versicolor": "#eb6834", "virginica": "#1baf7a"}
OUT = "sekiller/"
os.makedirs(OUT, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT + name + ".png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def box(ax, x, y, w, h, text, fc="#f5f8fb", ec=NAVY, tc=TEXT, fs=9.5, bold=False):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=fc, ec=ec, lw=1.2))
    ax.text(x, y, text, ha="center", va="center", color=tc, fontsize=fs, fontweight="bold" if bold else "normal",
            linespacing=1.35)


def arrow(ax, x1, y1, x2, y2, color=NAVY):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=13, color=color, lw=1.3))


def canvas(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis("off")
    return fig, ax


# 1) Yapay zekâ ⊃ makine öğrenmesi ⊃ derin öğrenme
fig, ax = canvas(7.4, 4.0, (0, 10.4), (0, 5.8))
for (cx, w, h, fc, ec) in [(5.2, 10.2, 5.6, "#eef5fc", NAVY), (6.55, 7.4, 4.5, "#dceaf8", "#2a78d6"),
                           (7.85, 4.6, 3.3, "#c3daf3", "#1c5cab")]:
    ax.add_patch(Ellipse((cx, 2.9), w, h, fc=fc, ec=ec, lw=1.4))
def lbl(x, t, sub):
    ax.text(x, 3.55, t, ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEXT, linespacing=1.3)
    ax.text(x, 2.1, sub, ha="center", va="center", fontsize=7.8, color=MUTED, linespacing=1.3)
lbl(1.5, "Yapay Zekâ\n(Artificial\nIntelligence)", "Kural tabanlı\nsistemler, arama\nalgoritmaları")
lbl(4.1, "Makine\nÖğrenmesi\n(Machine\nLearning)", "Karar ağacı,\nKNN, SVM,\nlojistik\nregresyon")
lbl(7.85, "Derin Öğrenme\n(Deep Learning)", "Çok katmanlı yapay\nsinir ağları\n(CNN, RNN, Transformer)")
save(fig, "ai_ml_dl")

# 2) Geleneksel programlama ve makine öğrenmesi
fig, ax = canvas(7.4, 3.5, (0, 12), (-0.4, 5.2))
def row(y0, title, l1, l2, mid, out):
    ax.text(0.1, y0 + 1.35, title, fontsize=10.5, fontweight="bold", color=NAVY)
    box(ax, 1.6, y0 + 0.5, 2.8, 0.8, l1, fs=9); box(ax, 1.6, y0 - 0.45, 2.8, 0.8, l2, fs=9)
    box(ax, 6, y0, 2.4, 1.1, mid, fc=NAVY, tc="white", bold=True)
    box(ax, 10.2, y0, 2.8, 0.95, out, fc="#eef8f1", ec="#3d9970", fs=9)
    arrow(ax, 3.05, y0 + 0.5, 4.75, y0 + 0.12); arrow(ax, 3.05, y0 - 0.45, 4.75, y0 - 0.12); arrow(ax, 7.25, y0, 8.75, y0)
row(3.4, "Geleneksel programlama", "Veri (girdi)", "Kurallar\n(programcı yazar)", "Program", "Cevaplar (çıktı)")
row(0.55, "Makine öğrenmesi", "Veri (girdi)", "Cevaplar (etiketler)", "Öğrenme\n(eğitim)", "Model\n(öğrenilen kurallar)")
save(fig, "trad_vs_ml")

# 3) Makine öğrenmesi iş akışı
fig, ax = canvas(7.6, 1.6, (0, 12.6), (0, 2))
steps = ["1. Veri\ntoplama", "2. Veri\nhazırlama", "3. Model\nseçimi", "4. Eğitim\n(fit)", "5. Test ve\ndeğerlendirme", "6. Tahmin\n(predict)"]
for i, s in enumerate(steps):
    x = 1.05 + i * 2.1
    box(ax, x, 1.0, 1.8, 1.15, s, fc=NAVY if i in (3, 5) else "#f5f8fb", tc="white" if i in (3, 5) else TEXT, fs=8.8)
    if i < 5:
        arrow(ax, x + 0.92, 1.0, x + 1.18, 1.0)
save(fig, "ml_workflow")

# 4) Öğrenme türleri
rng = np.random.default_rng(3)
fig, axs = plt.subplots(1, 3, figsize=(8.2, 2.9))
a = rng.normal([2, 2], 0.55, (25, 2)); b = rng.normal([4.2, 4], 0.55, (25, 2))
ax = axs[0]
ax.scatter(*a.T, s=26, c=C["setosa"], marker="o", edgecolors="white", lw=0.6, label="Sınıf A")
ax.scatter(*b.T, s=26, c=C["versicolor"], marker="s", edgecolors="white", lw=0.6, label="Sınıf B")
xx = np.linspace(0.5, 5.8, 10); ax.plot(xx, -xx + 6.1, color=TEXT, lw=1.3, ls="--")
ax.set_title("Denetimli öğrenme\n(etiketli veri → tahmin)", fontsize=9.5, color=TEXT)
ax.legend(fontsize=7.5, frameon=False, loc="upper center", ncol=2)
ax = axs[1]
pts = np.vstack([a, b, rng.normal([1.8, 4.6], 0.45, (20, 2))])
ax.scatter(*pts.T, s=26, c="#8d99a6", edgecolors="white", lw=0.6)
for cx, cy, r in [(2, 2, 1.5), (4.2, 4, 1.5), (1.8, 4.6, 1.15)]:
    ax.add_patch(Ellipse((cx, cy), r * 2, r * 1.75, fill=False, ec=NAVY, ls="--", lw=1.1))
ax.set_title("Denetimsiz öğrenme\n(etiketsiz veri → gruplar)", fontsize=9.5, color=TEXT)
for ax in axs[:2]:
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0, 6.3); ax.set_ylim(0, 7.4)
ax = axs[2]; ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
box(ax, 5, 8.0, 4.6, 1.6, "Ajan\n(agent)", fc=NAVY, tc="white", bold=True)
box(ax, 5, 2.4, 4.6, 1.6, "Ortam\n(environment)")
ax.add_patch(FancyArrowPatch((7.4, 7.8), (7.4, 2.6), connectionstyle="arc3,rad=-0.5", arrowstyle="-|>", mutation_scale=12, color=NAVY, lw=1.2))
ax.add_patch(FancyArrowPatch((2.6, 2.6), (2.6, 7.8), connectionstyle="arc3,rad=-0.5", arrowstyle="-|>", mutation_scale=12, color="#3d9970", lw=1.2))
ax.text(9.55, 5.2, "eylem", fontsize=8.5, color=NAVY, ha="center", rotation=-90)
ax.text(0.45, 5.2, "ödül / ceza\n+ yeni durum", fontsize=8.5, color="#2f7d58", ha="center", va="center", rotation=90)
ax.set_title("Pekiştirmeli öğrenme\n(deneme-yanılma → ödül)", fontsize=9.5, color=TEXT)
fig.tight_layout(); save(fig, "learning_types")

# 5) Sınıflandırma ve regresyon
fig, axs = plt.subplots(1, 2, figsize=(7.8, 3.0))
ax = axs[0]
ax.scatter(*a.T, s=26, c=C["setosa"], marker="o", edgecolors="white", lw=0.6, label="Normal e-posta")
ax.scatter(*b.T, s=26, c=C["versicolor"], marker="s", edgecolors="white", lw=0.6, label="Spam")
ax.plot(xx, -xx + 6.1, color=TEXT, lw=1.3, ls="--"); ax.text(5.2, 0.6, "karar sınırı", fontsize=8, color=MUTED, ha="center")
ax.set_xlabel("Özellik 1"); ax.set_ylabel("Özellik 2"); ax.set_xlim(0, 6.3); ax.set_ylim(0, 7.8)
ax.set_title("Sınıflandırma: çıktı bir KATEGORİ", fontsize=9.5, color=TEXT)
ax.legend(fontsize=7.5, frameon=False, loc="upper left", ncol=2)
ax = axs[1]
m2 = rng.uniform(50, 200, 40); price = 1.6 * m2 + rng.normal(0, 22, 40) + 20
ax.scatter(m2, price, s=22, c=C["setosa"], edgecolors="white", lw=0.6)
k, c0 = np.polyfit(m2, price, 1); g = np.linspace(50, 200, 10); ax.plot(g, k * g + c0, color=C["versicolor"], lw=2)
ax.set_xlabel("Ev büyüklüğü (m²)"); ax.set_ylabel("Fiyat (bin TL)")
ax.set_title("Regresyon: çıktı bir SAYI", fontsize=9.5, color=TEXT)
fig.tight_layout(); save(fig, "class_vs_reg")

# 6) Eğitim ve tahmin aşamaları
fig, ax = canvas(7.6, 2.9, (0, 12.4), (0, 4.6))
ax.text(0.05, 4.25, "Eğitim aşaması (training)", fontsize=10, fontweight="bold", color=NAVY)
box(ax, 1.75, 3.2, 3.2, 1.0, "Etiketli eğitim verisi\n(X_train, y_train)")
box(ax, 6.2, 3.2, 3.0, 1.0, "Algoritma\nmodel.fit(X, y)", fc=NAVY, tc="white", bold=True)
box(ax, 10.6, 3.2, 3.0, 1.0, "Eğitilmiş model", fc="#eef8f1", ec="#3d9970", bold=True)
arrow(ax, 3.4, 3.2, 4.65, 3.2); arrow(ax, 7.75, 3.2, 9.05, 3.2)
ax.text(0.05, 1.85, "Tahmin aşaması (prediction)", fontsize=10, fontweight="bold", color=NAVY)
box(ax, 1.75, 0.8, 3.2, 1.0, "Yeni, etiketsiz veri\n(X_new)")
box(ax, 6.2, 0.8, 3.0, 1.0, "Eğitilmiş model\nmodel.predict(X_new)", fc=NAVY, tc="white", bold=True)
box(ax, 10.6, 0.8, 3.0, 1.0, "Tahmin edilen sınıf\n(ör. \"spam\")", fc="#eef8f1", ec="#3d9970")
arrow(ax, 3.4, 0.8, 4.65, 0.8); arrow(ax, 7.75, 0.8, 9.05, 0.8)
ax.add_patch(FancyArrowPatch((10.6, 2.65), (6.6, 1.35), connectionstyle="arc3,rad=0.25", arrowstyle="-|>", mutation_scale=12, color=MUTED, lw=1.1, ls="--"))
save(fig, "train_predict")

# 7) Train-test split
fig, ax = canvas(7.4, 1.25, (-2, 152), (0, 2.2))
ax.add_patch(FancyBboxPatch((0, 0.6), 119, 1.0, boxstyle="round,pad=0,rounding_size=2", fc=NAVY, ec="white", lw=2))
ax.add_patch(FancyBboxPatch((121, 0.6), 29, 1.0, boxstyle="round,pad=0,rounding_size=2", fc="#3d9970", ec="white", lw=2))
ax.text(60, 1.1, "Eğitim verisi (training set) · %80 · 120 gözlem", ha="center", va="center", color="white", fontsize=9.5, fontweight="bold")
ax.text(135.5, 1.1, "Test · %20 · 30", ha="center", va="center", color="white", fontsize=9, fontweight="bold")
ax.text(60, 0.2, "Model bu veriyle öğrenir (fit)", ha="center", fontsize=8.5, color=MUTED)
ax.text(135.5, 0.2, "Başarı ölçülür", ha="center", fontsize=8.5, color=MUTED)
ax.text(75, 2.0, "Iris veri seti · 150 gözlem", ha="center", fontsize=9.5, color=TEXT, fontweight="bold")
save(fig, "train_test")

# 8) Underfitting / uygun / overfitting
rng = np.random.default_rng(7)
x = np.sort(rng.uniform(0, 1, 18)); y = np.sin(2 * np.pi * x) + rng.normal(0, 0.22, x.size)
grid = np.linspace(0, 1, 300)
fig, axs = plt.subplots(1, 3, figsize=(8.2, 2.6), sharey=True)
for ax, deg, title in zip(axs, [1, 4, 13], ["Underfitting (yetersiz öğrenme)", "Uygun model", "Overfitting (aşırı öğrenme)"]):
    coef = np.polyfit(x, y, deg)
    ax.scatter(x, y, s=22, c=C["setosa"], edgecolors="white", lw=0.6, zorder=3)
    yy = np.polyval(coef, grid); yy[np.abs(yy) > 2.1] = np.nan
    ax.plot(grid, yy, color=C["versicolor"], lw=2)
    ax.set_title(title, fontsize=9.5, color=TEXT); ax.set_xticks([]); ax.set_yticks([]); ax.set_ylim(-2.2, 2.2)
axs[0].text(0.5, -2.0, "Çok basit: deseni yakalayamıyor", ha="center", fontsize=8, color=MUTED)
axs[1].text(0.5, -2.0, "Genel eğilimi yakalıyor", ha="center", fontsize=8, color=MUTED)
axs[2].text(0.5, -2.0, "Gürültüyü ezberliyor", ha="center", fontsize=8, color=MUTED)
fig.tight_layout(); save(fig, "fitting")

# 9) Iris çiçeği anatomisi (şematik)
def leaf(ax, cx, cy, length, width, angle, fc, ec, z=2, alpha=1):
    t = np.deg2rad(angle)
    ex, ey = cx + np.cos(t) * length / 2, cy + np.sin(t) * length / 2
    ax.add_patch(Ellipse((ex, ey), length, width, angle=angle, fc=fc, ec=ec, lw=1.2, zorder=z, alpha=alpha))
    return ex, ey


def dim_arrow(ax, p1, p2, label, color, off=(0, 0), ha="center"):
    ax.annotate("", xy=p2, xytext=p1, arrowprops=dict(arrowstyle="<->", color=color, lw=1.4), zorder=6)
    m = ((p1[0] + p2[0]) / 2 + off[0], (p1[1] + p2[1]) / 2 + off[1])
    ax.text(*m, label, color=color, fontsize=9, fontweight="bold", ha=ha, va="center", zorder=7,
            bbox=dict(fc="white", ec="none", pad=1.2, alpha=0.9))


fig, ax = canvas(7.6, 5.8, (-6.2, 6.6), (-5.6, 5.2))
ax.plot([0, 0], [-5.4, -0.3], color="#4f8a3c", lw=4, zorder=1, solid_capstyle="round")
SEP_FC, SEP_EC, PET_FC, PET_EC = "#b9a6e3", "#5b3fa6", "#7d63c9", "#3e2a7a"
leaf(ax, 0, 0, 5.0, 2.2, -28, SEP_FC, SEP_EC, z=2)
leaf(ax, 0, 0, 5.0, 2.2, 208, SEP_FC, SEP_EC, z=2)
leaf(ax, 0, 0, 4.4, 2.0, -88, SEP_FC, SEP_EC, z=3)
leaf(ax, 0, 0.1, 3.6, 1.05, 72, PET_FC, PET_EC, z=4)
leaf(ax, 0, 0.1, 3.6, 1.05, 108, PET_FC, PET_EC, z=4)
leaf(ax, 0, 0.1, 3.9, 1.15, 90, PET_FC, PET_EC, z=5)
ax.add_patch(Ellipse((0, 0), 0.9, 0.7, fc="#f2c94c", ec="#b38a12", zorder=6))
t = np.deg2rad(-28); u = np.array([np.cos(t), np.sin(t)]); n = np.array([-np.sin(t), np.cos(t)])
OR = "#b0511f"
p0, p1 = 0.3 * u + 1.35 * n, 5.0 * u + 1.35 * n
dim_arrow(ax, tuple(p0), tuple(p1), "Sepal Length", OR, off=(0.55, 0.42))
c = 2.5 * u
dim_arrow(ax, tuple(c - 1.08 * n), tuple(c + 1.08 * n), "Sepal Width", OR, off=(1.15, -0.25))
dim_arrow(ax, (-0.95, 0.35), (-0.95, 4.05), "Petal Length", NAVY, off=(-1.25, 0.25))
dim_arrow(ax, (-0.58, 2.6), (0.58, 2.6), "Petal Width", NAVY, off=(1.75, 0.3))
ax.text(-6.0, 4.75, "Taç yaprak (Petal)", fontsize=11, fontweight="bold", color=PET_EC)
ax.text(-6.0, 4.25, "İçteki, dik duran 3 yaprak", fontsize=8.8, color=MUTED)
ax.plot([-3.0, -0.75], [4.15, 3.35], color=PET_EC, lw=0.9)
ax.text(2.4, -3.7, "Çanak yaprak (Sepal)", fontsize=11, fontweight="bold", color=SEP_EC)
ax.text(2.4, -4.2, "Dıştaki, aşağı sarkan 3 yaprak", fontsize=8.8, color=MUTED)
ax.plot([3.0, 2.7], [-3.35, -2.0], color=SEP_EC, lw=0.9)
ax.text(0.3, -5.1, "Sap", fontsize=9, color="#3b6b2c")
save(fig, "iris_anatomy")

# 10) Üç türün ortalama ölçülere göre ölçekli şeması (üstten görünüş)
iris = load_iris(); X, yv = iris.data, iris.target
fig, axs = plt.subplots(1, 3, figsize=(8.0, 3.2))
for k, (ax, name) in enumerate(zip(axs, iris.target_names)):
    sl, sw, pl, pw = X[yv == k].mean(axis=0)
    ax.set_xlim(-7.2, 7.2); ax.set_ylim(-7.2, 7.2); ax.set_aspect("equal"); ax.axis("off")
    for ang in (90, 210, 330):
        leaf(ax, 0, 0, sl, sw, ang, "#c9bdea", "#5b3fa6", z=2)
    for ang in (30, 150, 270):
        leaf(ax, 0, 0, pl, pw, ang, C[name], "#10263d", z=3)
    ax.add_patch(Ellipse((0, 0), 0.7, 0.7, fc="#f2c94c", ec="#b38a12", zorder=4))
    ax.set_title(f"Iris {name}", fontsize=11, fontweight="bold", color=TEXT, style="italic")
    ax.text(0, -7.0, f"Sepal: {sl:.2f} × {sw:.2f} cm\nPetal: {pl:.2f} × {pw:.2f} cm", ha="center", fontsize=8.5, color=MUTED)
fig.tight_layout(); save(fig, "iris_species")
print("Şekiller", OUT, "klasörüne kaydedildi.")
