# Example Repository for Custom Python Component

This is an example repository showing how you can use a custom Git repository for passing your own code into Keboola's Custom Python Component (CPC).

As the main source file in this repo is located in the `src` directory, the following line ensures importing other source files works the same way both when developing locally and when ran using CPC:

```py
sys.path.append(os.path.join(pathlib.Path(__file__).parent.parent))
```

Unlike our [another (preferred) example repository](/keboola/component-custom-python-example-repo-1), this example relies on the traditional `requirements.txt` file for defining dependencies. We strongly encourage you to move on and upgrade your workflows to modern tools like [uv](https://docs.astral.sh/uv), which make managing Python's projects far more reliable, repeatable & less error-prone. However, if you prefer to stick to the good ol' times, you can run this code locally by following these steps:

```sh
# 🐙 install keboola.component
pip install keboola.component
# 📦 install packages
pip install -r requirements.txt
# 🚀 run
python3 run src/main.py
```

You may encounter warnings when installing packages using pip for quite a some time already tried to discourage you from installing packages directly into your system Python environment. You have been warned. 🙂
