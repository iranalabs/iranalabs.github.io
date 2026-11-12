# Irana Labs website

Static website source for [iranalabs.com](https://iranalabs.com), published
from the public [`iranalabs/iranalabs.github.io`](https://github.com/iranalabs/iranalabs.github.io)
repository. The deployable site is in `site/`; App Store Connect copy and
screenshots are kept in `app-store/`.

## Preview locally

From the repository root, run:

```sh
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Publish with GitHub Pages

The workflow in `.github/workflows/pages.yml` deploys `site/` on every push to
`main` and can also be started manually. The repository's **Settings > Pages**
is configured to use **GitHub Actions**. The default Pages URL is
<https://iranalabs.github.io/>.

To use `iranalabs.com`, a repository administrator must set it as the custom
domain under **Settings > Pages**. A `CNAME` file in the deployed artifact does
not configure the domain for an Actions-based deployment. At the domain
registrar, configure the apex (`@`) with the four GitHub Pages A records:

```text
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

Optionally add the four IPv6 AAAA records:

```text
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

For `www.iranalabs.com`, add a CNAME pointing to `iranalabs.github.io`. Remove
registrar parking records that conflict with these values. DNS changes can take
time to propagate. Once Pages verifies the domain, enable **Enforce HTTPS** and
check both the apex and `www` hostname.

The official setup guidance is
[GitHub Pages custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## App Store screenshots

The original Demo Mode captures are under `app-store/source/`. After replacing
them with updated simulator or device captures, regenerate the branded,
opaque JPEGs used on the site and in App Store Connect:

```sh
python3 scripts/build_store_screenshots.py
```

The script requires librsvg (`rsvg-convert`) and ImageMagick (`magick`), and
writes to `site/assets/screenshots/`.

## Site pages

- `/` - Irana Labs
- `/apps/` - Apps
- `/apps/irana-cams/` - iRana Cams
- `/apps/irana-cams/privacy/` - iRana Cams privacy policy
- `/apps/irana-cams/support/` - iRana Cams support
