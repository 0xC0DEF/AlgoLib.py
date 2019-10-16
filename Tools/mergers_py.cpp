#include "DirectedGraph.h"

using namespace std;

DirectedGraph g(200);
unordered_map<int, bool> im;
map<string, int> s2i;
map<int, string> i2s;
void regi(const string &s)
{
	if (s2i.find(s) == s2i.end())
	{
		int idx = (int)s2i.size();
		i2s[idx] = s;
		s2i[s] = idx;
				im[idx]=true;
	}
}

set<string> stdmodule={"sys","functools","math"};

void solve(const string &fname, const string &hdir)
{
	regi(fname);
	ifstream in(fname + ".py");
	char buf[1000];
	while (in.getline(buf, sizeof buf))
	{
		if (string(buf, 5) == "from ")
		{
			auto it = buf + 5;
			while (*it == ' ' || *it == '\t')
				it++;
			string s;
			while(*it != ' ')
				s.push_back(*it++);
			if (stdmodule.count(s))
				continue;
			solve(s, hdir);
			g.add_edge(s2i[fname], s2i[s]);
		}
	}
	in.close();
}

int main(int argc, char ** argv){
	string fn, hdir="./";
	if (argc < 2)	{
		cout << "source file: ";
		cin >> fn;
	}
	else if (argc == 2)	{
		fn = argv[1];
		if (fn.substr(fn.size() - 3, 3) == ".py")
			fn=fn.substr(0,fn.size() - 3);
	}
	else	{
		cout << "Usage1 : merger.exe" << endl;
		cout << "Usage2 : merger.exe <MAIN_SOURCE_FILE>" << endl;
		return 0;
	}
	solve(fn, hdir);
	auto ord = g.topo_sort();
	reverse(all(ord));
	ofstream out("merged.py");
	for (auto i : ord)
	{
		if(!im[i])
			continue;
		ifstream in(i2s[i] + ".py");
		char buf[1000];
		while (in.getline(buf, sizeof buf))
		{
			if (string(buf, strlen("from ")) == "from ")
			{
				auto it = buf + 5;
				while (*it == ' ' || *it == '\t')
					it++;
				string s;
				while(*it != ' ')
					s.push_back(*it++);
				if (!stdmodule.count(s))
					continue;
			}
			out << buf << endl;
		}
		in.close();
	}
	out.close();

	return 0;
}